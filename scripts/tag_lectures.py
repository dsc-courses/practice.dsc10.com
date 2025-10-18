# scripts/tag_lectures.py
import csv, json, re, sys, argparse, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROB_DIR = ROOT / "problems"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(.*)\Z", re.DOTALL)

TERM_RE   = r"(fa|wi|sp|su)\d{2}"
EXAM_RE   = re.compile(rf"^{TERM_RE}-(midterm|final)$")
QUIZ_ROOT = re.compile(rf"^{TERM_RE}-quizzes$")         
QUIZ_DIR  = re.compile(r"^quiz(\d+)$", re.IGNORECASE)   

def norm_header(h: str) -> str:
    """normalize headers like 'QUARTER-EXAM' -> 'quarter_exam'"""
    return re.sub(r"[^a-z0-9]+", "_", h.strip().lower()).strip("_")

def get_field(row: dict, *candidates):
    """fetch row field by trying normalized header aliases"""
    norm = {norm_header(k): v for k, v in row.items()}
    for c in candidates:
        if c in norm:
            return norm[c]
    raise KeyError(f"Missing required column. Tried aliases: {candidates}")

def parse_lectures(val) -> list[int]:
    """accept '14', '14,18', '14, 18', or JSON like '[14,18]'."""
    if val is None:
        return []
    s = str(val).strip()
    if not s:
        return []
    # JSON array?
    if s.startswith("[") and s.endswith("]"):
        try:
            arr = json.loads(s)
            return [int(x) for x in arr]
        except Exception:
            pass
    # comma/space separated
    parts = re.split(r"[,\s]+", s)
    out = []
    for p in parts:
        if p == "":
            continue
        out.append(int(p))
    return out

def load_mapping(path: pathlib.Path):
    """
    Returns: dict[str, dict[int, list[int]]]
    mapping[slug][qnum] = [lec1, lec2, ...]
    slug examples:
      - 'sp24-final', 'wi25-midterm'
      - 'fa24-quiz1'  (NOTE: quizzes use quiz number in slug)
    """
    m: dict[str, dict[int, list[int]]] = {}
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as f:
            rdr = csv.DictReader(f)
            for row in rdr:
                slug = str(get_field(
                    row,
                    "quarter_exam", "quarter_exam_id", "quarter", "quarter_exam_slug",
                    "quarter_exam_name", "quarter_exam_folder", "quarter_exam_dir",
                    "slug"
                )).strip()
                if not slug:
                    continue
                q = int(str(get_field(row, "question", "q", "question_number")).strip())
                lecs = parse_lectures(get_field(row, "lecture", "lectures", "lecture_numbers"))
                if not lecs:
                    continue
                m.setdefault(slug, {}).setdefault(q, [])
                # append unique
                for L in lecs:
                    if L not in m[slug][q]:
                        m[slug][q].append(L)
    elif path.suffix.lower() == ".json":
        raw = json.loads(path.read_text(encoding="utf-8"))
        for item in raw:
            # accept either quarterExam or quarter_exam
            slug = item.get("quarterExam") or item.get("quarter_exam") or item.get("slug")
            q = int(item["question"])
            lecs = item.get("lectures") or item.get("lecture")
            lecs = parse_lectures(lecs)
            if not slug or not lecs:
                continue
            m.setdefault(slug, {}).setdefault(q, [])
            for L in lecs:
                if L not in m[slug][q]:
                    m[slug][q].append(L)
    else:
        raise SystemExit(f"Unsupported mapping format: {path.suffix}")
    return m

def parse_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text  # no front matter; content is whole file
    front_raw, body = m.group(1), m.group(2)
    data = yaml.safe_load(front_raw) or {}
    if not isinstance(data, dict):
        data = {}
    return data, body

def build_text(front: dict, body: str):
    fm = yaml.safe_dump(front, sort_keys=False).strip()
    return f"---\n{fm}\n---\n\n{body.lstrip()}"

def find_qnum(fname: str):
    """
    Parse question number from filenames like:
      q06.md, q6.md, q06-copy.md, q06-disc07.md, etc.
    """
    m = re.match(r"^q0*([0-9]+)\b.*\.md\Z", fname)
    return int(m.group(1)) if m else None

def derive_slug(md_path: pathlib.Path) -> str | None:
    """
    Derive slug from a problem file path.

    Supports:
      problems/sp24-final/q06.md            -> 'sp24-final'
      problems/wi25-midterm/q03.md         -> 'wi25-midterm'
      problems/fa24-quizzes/quiz1/q02.md   -> 'fa24-quiz1'
    """
    parent = md_path.parent            # qNN.md's directory
    name   = parent.name

    # midterm/final: directory itself is the slug (e.g., 'sp24-final')
    if EXAM_RE.match(name):
        return name

    # quizzes: parent is 'quizK', grandparent is '<term><yy>-quizzes'
    gp = parent.parent
    if gp and QUIZ_ROOT.match(gp.name):
        m_quiz = QUIZ_DIR.match(name)
        if m_quiz:
            quiz_no = int(m_quiz.group(1))
            term = gp.name.split("-")[0]  # e.g., 'fa24'
            return f"{term}-quiz{quiz_no}"

    # unknown layout (disc/probset/etc.) – not in mapping by default
    return None

def normalize_lecture_field(value):
    """
    Ensure final YAML is either int or a sorted unique list[int].
    If a list has length 1 -> store as int for compactness.
    """
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, list):
        uniq = sorted({int(x) for x in value})
        return uniq[0] if len(uniq) == 1 else uniq
    # string, etc -> try to parse
    lecs = parse_lectures(value)
    if not lecs:
        return None
    return lecs[0] if len(lecs) == 1 else sorted(set(lecs))

def main():
    ap = argparse.ArgumentParser(
        description="Tag problems with lecture numbers from a central mapping (supports midterm/final/quizzes and multi-lecture)."
    )
    ap.add_argument("mapping", help="Path to data/lecture_map.csv or .json")
    ap.add_argument("--apply", action="store_true", help="Write changes (default is dry-run)")
    ap.add_argument("--force", action="store_true", help="Overwrite (do not union) existing 'lecture' tags")
    args = ap.parse_args()

    mapping = load_mapping(pathlib.Path(args.mapping))
    changed = 0
    missing = 0
    total = 0

    for md in PROB_DIR.rglob("q*.md"):
        total += 1

        q = find_qnum(md.name)
        if q is None:
            print(f"[skip] {md} (can't parse question number)")
            continue

        slug = derive_slug(md)
        if not slug:
            # Not an exam/quiz problem (disc/probset/etc.) — skip quietly
            missing += 1
            continue

        lecs = mapping.get(slug, {}).get(q)
        if not lecs:
            missing += 1
            continue

        text = md.read_text(encoding="utf-8")
        front, body = parse_frontmatter(text)

        existing = front.get("lecture", None)
        if existing is not None and not args.force:
            # merge (union) with existing; support int or list in existing
            if isinstance(existing, int):
                merged = sorted(set([existing] + lecs))
            elif isinstance(existing, list):
                merged = sorted(set([int(x) for x in existing] + lecs))
            else:
                merged = sorted(set(parse_lectures(existing) + lecs))
            front["lecture"] = normalize_lecture_field(merged)
        else:
            # set from mapping (possibly multi)
            front["lecture"] = normalize_lecture_field(lecs)

        new_text = build_text(front, body)

        if args.apply:
            md.write_text(new_text, encoding="utf-8")
            print(f"[write] {md} ← lecture: {front['lecture']}")
        else:
            print(f"[dry]   {md} would set lecture: {front['lecture']}")

        changed += 1

    print(f"\nDone. total={total} changed={changed} missing_in_mapping={missing}")
    if not args.apply:
        print("Dry run only. Re-run with --apply to write changes.")

if __name__ == "__main__":
    sys.exit(main())
