"""Catch hand edits to docs/.

docs/ is what `uv run run.py` builds. The published site is rebuilt from
problems/, pages/, index.md, assets/ and pdfs/, so anything written straight into
docs/ would be lost. Deleting files there is fine.

    python3 scripts/check_docs_untouched.py [--warn] BASE HEAD

Compares HEAD with its merge base with BASE, so only the change's own commits
count. Without --warn (pull requests) it exits 1 on a hand edit. With --warn
(pushes) it prints a GitHub warning and exits 0: by then the edit is already on
master, the build overwrites docs/ anyway, and failing would keep the push's
source changes from publishing. Uses only the standard library, so it runs
before `uv sync`.
"""
import subprocess
import sys

NO_COMMIT = {"", "0" * 40}

WHERE = """docs/ is built from the source files, and the site is published from a fresh
build, so edits made there are lost. Make the change in the source instead:
problems/ (problem text and solutions), pages/ (a page's title, intro, banners
and problem list), index.md (the homepage), assets/ (images, CSS) or pdfs/."""

FAIL = """
These files under docs/ were edited or added by hand:

{files}

{where}

To take the docs/ changes out of this pull request:

  git checkout $(git merge-base HEAD origin/master) -- docs
  git commit -m "Undo docs/ edits"
  git push

If you added new files under docs/, also `git rm` them. If you previewed locally
with `uv run run.py`, run `git restore docs` before committing next time.
"""

WARN = """::warning title=docs/ was edited by hand::These files under docs/ were edited or added by hand and will be overwritten by the build: {inline}
{where}

Files:
{files}

Nothing to undo: the published site is rebuilt from source. If these edits were
meant to show on the site, redo them in the source files.
"""


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


def changed_docs_files(base, head):
    """The files under docs/ that HEAD adds or modifies since its merge base with BASE, or None if git can't tell."""
    merge_base = git("merge-base", base, head)
    if merge_base.returncode != 0:
        return None
    diff = git("diff", "--name-only", "--no-renames", "--diff-filter=d", merge_base.stdout.strip(), head, "--", "docs")
    if diff.returncode != 0:
        return None
    return [line for line in diff.stdout.splitlines() if line]


def main(argv):
    args = argv[1:]
    warn = "--warn" in args
    args = [a for a in args if a != "--warn"]
    if len(args) != 2:
        print(__doc__)
        return 2
    base, head = args
    if base in NO_COMMIT:
        print("No earlier commit to compare with (new branch or manual run); skipping the docs/ check.")
        return 0
    files = changed_docs_files(base, head)
    if files is None:
        print(f"Can't compare with {base[:12]} (it may have been force-pushed away); skipping the docs/ check.")
        return 0
    if not files:
        print("docs/ was not edited by hand.")
        return 0
    listing = "\n".join(f"  {f}" for f in files)
    if warn:
        print(WARN.format(inline=", ".join(files[:10]) + (" ..." if len(files) > 10 else ""), where=WHERE, files=listing))
        return 0
    print(FAIL.format(files=listing, where=WHERE))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
