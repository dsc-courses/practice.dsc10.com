# scripts/fill_averages.py
"""
Fill in <average> tags for one exam or quiz from a Gradescope scores export.

    python scripts/fill_averages.py scores.csv fa25-final          # preview only
    python scripts/fill_averages.py scores.csv fa25-final --apply  # write the .md files

Score columns look like '3.2: 3a blank b (3.0 pts)' (question 3, subpart a) or
'3.2 (3.0 pts)' (question 3, second subpart). Columns for the same subpart are
combined, blank cells are skipped, and 0-point columns are ignored.

Score exports identify students, so this script only reads the score columns
and never prints or stores anything about individual students. Keep exports out
of git (e.g. in .git/info/exclude).
"""
import argparse, csv, pathlib, re, string, sys, yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]

COLUMN_RE = re.compile(r"^(\d+)\.\d+:\s*(\d+)\s*([a-z])?\b.*\(([\d.]+) pts?\)\s*$")
NUMBERED_RE = re.compile(r"^(\d+)\.(\d+)\s*\(([\d.]+) pts?\)\s*$")
WHOLE_QUESTION_RE = re.compile(r"^(\d+)(?::.*?)?\s*\(([\d.]+) pts?\)\s*$")
HAS_POINTS_RE = re.compile(r"\([\d.]+ pts?\)")
SUBPROB_RE = re.compile(r"^# BEGIN SUBPROB.*?^# END SUBPROB", re.DOTALL | re.MULTILINE)
END_SOLUTION_RE = re.compile(r"^# END (?:SOLUTION|SOLN)[ \t]*\r?$", re.MULTILINE)
AVERAGE_RE = re.compile(r"<average>\d*</average>")
POINTS_RE = re.compile(r"\*\*\((\d+(?:\.\d+)?) pts?\)\*\*")


def stop(message):
    sys.exit(f"Stopped, no files changed: {message}")


def parse_column(name):
    """Return (question, letter or None, points) for a score column, else None."""
    m = COLUMN_RE.match(name.strip())
    if m:
        if m.group(1) != m.group(2):
            stop(f"column '{name}' numbers its question two different ways")
        return int(m.group(1)), m.group(3), float(m.group(4))
    m = NUMBERED_RE.match(name.strip())
    if m:
        part = int(m.group(2))
        if not 1 <= part <= len(string.ascii_lowercase):
            stop(f"can't tell which subpart column '{name}' belongs to")
        return int(m.group(1)), string.ascii_lowercase[part - 1], float(m.group(3))
    m = WHOLE_QUESTION_RE.match(name.strip())
    if m:
        return int(m.group(1)), None, float(m.group(2))
    if HAS_POINTS_RE.search(name):
        stop(f"can't tell which question column '{name}' belongs to")
    return None


def load_scores(path):
    """Return {question: {letter or None: (mean score, points available)}}."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    scores = {}
    total_points = 0
    for i, name in enumerate(header):
        parsed = parse_column(name)
        if parsed is None:
            continue
        question, letter, points = parsed
        if points == 0:
            print(f"Skipping 0-point column '{name}'")
            continue

        values = []
        for row_num, row in enumerate(rows, start=2):
            cell = row[i].strip() if i < len(row) else ""
            if cell == "":
                continue
            try:
                values.append(float(cell))
            except ValueError:
                stop(f"non-numeric score in column '{name}', line {row_num}")
        if not values:
            stop(f"no scores in column '{name}'")

        mean, available = scores.setdefault(question, {}).get(letter, (0, 0))
        scores[question][letter] = (mean + sum(values) / len(values), available + points)
        total_points += points

    if not scores:
        stop("no score columns found, expected names like '1.1: 1a (3.0 pts)'")

    if "Max Points" in header:
        i = header.index("Max Points")
        maxes = {row[i].strip() for row in rows if i < len(row) and row[i].strip()}
        if len(maxes) == 1 and float(maxes.pop()) != total_points:
            stop(f"score columns add up to {total_points} points, but 'Max Points' disagrees")
    return scores


def load_problem_paths(slug):
    """Return the problem files of a page in order, so index 0 is question 1."""
    pages = list((ROOT / "pages").glob(f"*/{slug}.yml"))
    if len(pages) != 1:
        stop(f"expected one page named {slug}.yml, found {len(pages)}")
    params = yaml.safe_load(pages[0].read_text(encoding="utf-8"))
    return [ROOT / "problems" / f"{entry.split(', ')[0]}.md" for entry in params["problems"]]


def add_average(block, average, force):
    """Return (new block, status) for the text of one subpart or whole problem."""
    existing = AVERAGE_RE.findall(block)
    if existing and not force:
        return block, "keep"
    if len(existing) > 1:
        return None, "more than one <average> tag"

    tag = f"<average>{average}</average>"
    if existing:
        return AVERAGE_RE.sub(tag, block), "replace"

    ends = list(END_SOLUTION_RE.finditer(block))
    if len(ends) != 1:
        return None, f"expected one END SOLUTION, found {len(ends)}"
    start = ends[0].start()
    newline = "\r\n" if "\r\n" in block else "\n"
    gap = "" if block[:start].endswith(newline * 2) else newline
    return f"{block[:start]}{gap}{tag}{newline}{newline}{block[start:]}", "add"


def fill_problem(path, question, parts, force):
    """Return (new text, report rows), after checking the file matches the CSV."""
    label = path.relative_to(ROOT)
    if not path.exists():
        stop(f"{label} does not exist")
    with open(path, newline="", encoding="utf-8") as f:
        text = f.read()

    subprobs = list(SUBPROB_RE.finditer(text))
    if subprobs:
        letters = list(string.ascii_lowercase[:len(subprobs)])
    else:
        letters = [None]
    if set(parts) != set(letters):
        stop(f"question {question}: the CSV has parts {sorted(str(p) for p in parts)}, "
             f"but {label} has {sorted(str(l) for l in letters)}")

    spans = [(m.start(), m.end()) for m in subprobs] or [(0, len(text))]
    report = []
    # Work backwards so earlier spans stay valid as text is inserted.
    for letter, (start, end) in reversed(list(zip(letters, spans))):
        mean, points = parts[letter]
        block = text[start:end]

        listed = [float(p) for p in POINTS_RE.findall(block)]
        if listed and sum(listed) != points:
            stop(f"question {question}{letter or ''}: the CSV says {points} points, "
                 f"but {label} says {sum(listed)}")

        average = int(mean / points * 100 + 0.5)
        new_block, status = add_average(block, average, force)
        if new_block is None:
            stop(f"question {question}{letter or ''} in {label}: {status}")
        text = text[:start] + new_block + text[end:]
        report.append((f"{question}{letter or ''}", mean, points, average, status))
    return text, report[::-1]


def main():
    ap = argparse.ArgumentParser(description="Fill in <average> tags from a Gradescope scores export.")
    ap.add_argument("scores", help="Path to the scores CSV")
    ap.add_argument("page", help="Page name, e.g. fa25-final or sp26-quiz1")
    ap.add_argument("--apply", action="store_true", help="Write changes (default is a preview)")
    ap.add_argument("--force", action="store_true", help="Overwrite existing averages")
    args = ap.parse_args()

    scores = load_scores(args.scores)
    paths = load_problem_paths(args.page)
    if sorted(scores) != list(range(1, len(paths) + 1)):
        stop(f"the CSV has questions {sorted(scores)}, but {args.page} has questions 1 to {len(paths)}")

    # Check every question before writing anything.
    updates = []
    print(f"{'Part':6}{'Mean':>8}{'Points':>8}{'Average':>9}  Status")
    for question, path in enumerate(paths, start=1):
        new_text, report = fill_problem(path, question, scores[question], args.force)
        updates.append((path, new_text))
        for part, mean, points, average, status in report:
            print(f"{part:6}{mean:8.2f}{points:8.1f}{average:8d}%  {status}")

    changed = 0
    for path, new_text in updates:
        with open(path, newline="", encoding="utf-8") as f:
            if f.read() == new_text:
                continue
        changed += 1
        if args.apply:
            with open(path, "w", newline="", encoding="utf-8") as f:
                f.write(new_text)

    if args.apply:
        print(f"\nWrote {changed} file(s). Rebuild to update the site:")
        page_path = next((ROOT / "pages").glob(f"*/{args.page}.yml")).relative_to(ROOT)
        print(f"  python run.py {page_path}")
        print('  python -c "import run; run.write_lecture_pages()"')
    else:
        print(f"\nPreview only: {changed} file(s) would change. Re-run with --apply to write them.")


if __name__ == "__main__":
    main()
