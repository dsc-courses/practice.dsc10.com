"""A merge conflict that gets committed unresolved shows up on the live site as
"<<<<<<< HEAD ... >>>>>>>" text (fa25 quiz 5 on the homepage, sp26 quiz 1 q1).
Fail CI when any source file still has conflict markers."""
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

TEXT_EXTENSIONS = {".md", ".yml", ".yaml", ".py", ".js", ".css", ".html", ".json", ".toml", ".csv", ".txt", ".tex"}

# "<<<<<<< HEAD" / ">>>>>>> abc123" (or "Stashed changes" etc.) are unambiguous.
# A bare "=======" line could be a Markdown heading underline, so it only counts
# in a file that also has one of the other two.
OPEN_CLOSE = re.compile(r"^(<<<<<<<|>>>>>>>)( |$)")
MIDDLE = re.compile(r"^=======$")


def conflict_lines(text):
    """Line numbers (1-based) of leftover conflict markers in text."""
    lines = text.splitlines()
    hits = [i for i, line in enumerate(lines, 1) if OPEN_CLOSE.match(line)]
    if hits:
        hits += [i for i, line in enumerate(lines, 1) if MIDDLE.match(line)]
    return sorted(hits)


def source_files():
    """Tracked text files, minus docs/ (build output, rebuilt from these)."""
    out = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, check=True, capture_output=True, text=True).stdout
    for name in out.split("\0"):
        if name and not name.startswith("docs/") and Path(name).suffix.lower() in TEXT_EXTENSIONS:
            yield name


def test_no_source_file_has_conflict_markers():
    problems = []
    for name in source_files():
        path = REPO / name
        if not path.exists():  # deleted in the working tree but not yet committed
            continue
        hits = conflict_lines(path.read_text(encoding="utf-8", errors="replace"))
        if hits:
            problems.append(f"{name}: lines {', '.join(map(str, hits))}")
    assert not problems, (
        "Unresolved merge conflict markers (<<<<<<< / ======= / >>>>>>>). "
        "Pick the version to keep and delete the marker lines:\n  " + "\n  ".join(problems)
    )


def test_checks_markdown_and_yaml_but_not_docs():
    files = set(source_files())
    assert "index.md" in files
    assert any(f.startswith("pages/") and f.endswith(".yml") for f in files)
    assert any(f.startswith("problems/") for f in files)
    assert not any(f.startswith("docs/") for f in files)


def test_catches_a_committed_conflict():
    text = (
        "**Answer**: `x == wc.shape[0]`\n\n"
        "<<<<<<< HEAD\nExplanation: one.\n=======\n    Explanation: one.\n"
        ">>>>>>> 5aed95570d0459d710365a51a4f6f7b8e84255c0\n"
    )
    assert conflict_lines(text) == [3, 5, 7]


def test_catches_a_stash_conflict():
    text = "<td>\n<<<<<<< Updated upstream\n</td>\n=======\n>>>>>>> Stashed changes\n"
    assert conflict_lines(text) == [2, 4, 5]


def test_a_markdown_heading_underline_is_not_a_conflict():
    assert conflict_lines("Data description\n=======\n\nSome text.\n") == []


def test_arrows_inside_a_line_are_not_a_conflict():
    assert conflict_lines("```py\n>>> df.shape\n```\nThe result <<<<<<< is odd but fine.\n") == []
