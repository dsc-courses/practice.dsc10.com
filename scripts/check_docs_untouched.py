"""Fail if a change edits or adds files under docs/.

docs/ is what `uv run run.py` builds. The published site is rebuilt from
problems/, pages/, index.md, assets/ and pdfs/, so anything written straight into
docs/ would be lost. Deleting files there is fine.

    python3 scripts/check_docs_untouched.py BASE HEAD

Compares HEAD with its merge base with BASE, so only the change's own commits
count. Uses only the standard library so it runs before `uv sync`.
"""
import subprocess
import sys

NO_COMMIT = {"", "0" * 40}

HELP = """
These files under docs/ were edited or added by hand:

{files}

docs/ is built from the source files, and the site is published from a fresh
build, so these edits would be lost. Instead:

  1. Make the change in the source: problems/ (problem text and solutions),
     pages/ (a page's title, intro, banners and problem list), index.md (the
     homepage), assets/ (images, CSS) or pdfs/.
  2. Undo the docs/ changes and commit that:
       git checkout origin/master -- docs
       git commit -m "Undo docs/ edits"
     (If you added a new file under docs/, also `git rm` it.)
  3. Push. If you previewed locally with `uv run run.py`, run `git restore docs`
     before committing next time.
"""


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def changed_docs_files(base, head):
    merge_base = git("merge-base", base, head).strip()
    out = git("diff", "--name-only", "--no-renames", "--diff-filter=d", merge_base, head, "--", "docs")
    return [line for line in out.splitlines() if line]


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    base, head = argv[1], argv[2]
    if base in NO_COMMIT:
        print("No earlier commit to compare with (new branch or manual run); skipping the docs/ check.")
        return 0
    files = changed_docs_files(base, head)
    if not files:
        print("docs/ was not edited by hand.")
        return 0
    print(HELP.format(files="\n".join(f"  {f}" for f in files)))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
