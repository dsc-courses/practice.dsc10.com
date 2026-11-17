"""Find anything a student could see or use on one copy of the site that's missing from another.

Used before publishing from GitHub Actions: tutors have edited docs/ by hand, and
a build from source must not silently drop those edits.

    uv run scripts/compare_site.py REFERENCE BUILT

REFERENCE is the site as it's served now (usually docs/ on master) and BUILT is a
fresh build from source (`uv run run.py` in a clean checkout, or the
github-pages artifact from the "Build and Publish" workflow). It prints
everything in REFERENCE that BUILT lacks and exits 1 if there is any.

For each HTML page it compares what matters to a student, not raw bytes, so
whitespace and markup reshuffles from pandoc don't count:
  - visible text, as a sequence of words (so line wrapping doesn't matter)
  - every link, image, video, iframe, stylesheet and script URL
  - inline <script> and <style> blocks (the timer, progress tracker, etc.)
  - the attributes those scripts hook onto (id, data-*, and the button/input type)
Every other file (PDFs, images, CSS, JS) must exist in BUILT with the same bytes.
Things BUILT has that REFERENCE lacks are new content and never count as a problem.
"""
import difflib
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

URL_ATTRS = {
    "a": "href",
    "img": "src",
    "iframe": "src",
    "video": "src",
    "source": "src",
    "audio": "src",
    "embed": "src",
    "object": "data",
    "link": "href",
    "script": "src",
}

# Files the build owns that legitimately differ between builds or aren't content.
IGNORED_FILES = {".DS_Store", ".nojekyll"}


def _norm(text):
    return re.sub(r"\s+", " ", text).strip()


def _code(text):
    """Script/style text with whitespace and blank lines removed, so reformatting doesn't count."""
    return "\n".join(_norm(line) for line in text.splitlines() if line.strip())


def page_features(html):
    """What a student can see or use on one page, as a Counter of (kind, value) pairs."""
    soup = BeautifulSoup(html, "lxml")
    features = Counter()

    for tag, attr in URL_ATTRS.items():
        for el in soup.find_all(tag):
            value = el.get(attr)
            if value and not value.startswith("#"):
                features[("url", value.strip())] += 1

    for el in soup.find_all(["script", "style"]):
        if el.get("src"):
            continue
        body = _code(el.get_text())
        if body:
            features[(f"inline-{el.name}", hashlib.sha256(body.encode()).hexdigest()[:12] + " " + body[:80])] += 1

    for el in soup.find_all(True):
        for name, value in el.attrs.items():
            if name.startswith("data-") or (name == "id" and el.name in ("button", "input", "select", "details", "div", "span", "section")):
                if isinstance(value, list):
                    value = " ".join(value)
                features[("attr", f"{el.name}[{name}={value}]")] += 1
        if el.name in ("button", "input", "select", "textarea"):
            features[("control", f"{el.name} {el.get('type', '')} {_norm(el.get_text())}".strip())] += 1

    return features


def page_words(html):
    """The page's visible text as a list of words, in reading order."""
    soup = BeautifulSoup(html, "lxml")
    for el in soup.find_all(["script", "style", "noscript", "template"]):
        el.decompose()
    body = soup.body or soup
    return body.get_text(" ").split()


def missing_text(ref_words, built_words):
    """Runs of words in ref_words that built_words drops or replaces, in reading order."""
    matcher = difflib.SequenceMatcher(None, ref_words, built_words, autojunk=False)
    runs = []
    for op, i1, i2, _, _ in matcher.get_opcodes():
        if op in ("delete", "replace"):
            runs.append(" ".join(ref_words[i1:i2]))
    return runs


def compare_page(ref_html, built_html):
    """Everything on the reference page that the built page lacks, as a list of (kind, value, missing count)."""
    ref, built = page_features(ref_html), page_features(built_html)
    missing = sorted((kind, value, n) for (kind, value), n in (ref - built).items())
    text = [("text", run, 1) for run in missing_text(page_words(ref_html), page_words(built_html))]
    return text + missing


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare_sites(ref_root, built_root):
    """Returns {relative path: [problems]} for every file in ref_root that built_root loses or changes."""
    ref_root, built_root = Path(ref_root), Path(built_root)
    report = {}
    for ref_file in sorted(ref_root.rglob("*")):
        if not ref_file.is_file() or ref_file.name in IGNORED_FILES:
            continue
        rel = ref_file.relative_to(ref_root)
        built_file = built_root / rel
        if not built_file.is_file():
            report[str(rel)] = [("file", "missing from the build", 1)]
            continue
        if ref_file.suffix == ".html":
            problems = compare_page(
                ref_file.read_text(encoding="utf-8", errors="replace"),
                built_file.read_text(encoding="utf-8", errors="replace"),
            )
        elif _sha(ref_file) != _sha(built_file):
            problems = [("file", "contents differ", 1)]
        else:
            problems = []
        if problems:
            report[str(rel)] = problems
    return report


def format_report(report, limit_per_file=25):
    lines = []
    for rel, problems in report.items():
        lines.append(f"\n{rel}")
        for kind, value, n in problems[:limit_per_file]:
            extra = f" (x{n})" if n > 1 else ""
            lines.append(f"  - [{kind}] {value[:200]}{extra}")
        if len(problems) > limit_per_file:
            lines.append(f"  ... and {len(problems) - limit_per_file} more")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    report = compare_sites(argv[1], argv[2])
    if not report:
        print("Nothing in the reference site is missing from the build.")
        return 0
    print(format_report(report))
    print(f"\n{len(report)} file(s) lose content in the build.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
