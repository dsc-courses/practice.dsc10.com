"""Shared test setup: a tiny copy of the site, and helpers for running run.py on it."""
import importlib
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]

GOOD_PROBLEM = """---
lecture: 1
---

# BEGIN PROB

What is $x^2$ when $x = 3$?

![A picture](../assets/images/fa99-midterm/pic.png)

# BEGIN SOLUTION

**Answer**: GOOD-ANSWER-TEXT

<average>61</average>

# END SOLUTION

# END PROB
"""

MISSING_SOLUTION = """# BEGIN PROB

This problem has no solution block.

# END PROB
"""

# Tagged for a lecture, so lecture pages must process it with solutions shown.
TAGGED_MISSING_SOLUTION = "---\nlecture: 1\n---\n\n" + MISSING_SOLUTION

MISMATCHED_TAGS = """# BEGIN PROB

This problem never closes.

# BEGIN SOLUTION

**Answer**: 1

# END SOLUTION
"""


def page_yml(problems, show_solution=True, title="Test Page"):
    lines = [
        f'title: "{title}"',
        'instructors: "Test Instructor"',
        'context: "Test context."',
        f"show_solution: {str(show_solution).lower()}",
        "problems:",
    ]
    lines += [f"  - {name}" for name in problems]
    return "\n".join(lines) + "\n"


class Site:
    """A tiny, self-contained site in a temporary folder."""

    def __init__(self, root):
        self.root = Path(root)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def run(self, *args, path_dirs=(), pythonpath=None):
        """Run run.py with no real pandoc on PATH unless a test adds one."""
        empty = self.root.parent / "empty-bin"
        empty.mkdir(exist_ok=True)
        env = dict(os.environ)
        env["PATH"] = os.pathsep.join([*map(str, path_dirs), str(empty)])
        env.pop("PYTHONPATH", None)
        if pythonpath:
            env["PYTHONPATH"] = str(pythonpath)
        return subprocess.run(
            [sys.executable, "run.py", *args],
            cwd=self.root,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )


@pytest.fixture
def site(tmp_path):
    root = tmp_path / "site"
    root.mkdir()
    shutil.copy(REPO / "run.py", root / "run.py")
    shutil.copy(REPO / "include-head.html", root / "include-head.html")
    shutil.copytree(REPO / "utils", root / "utils", ignore=shutil.ignore_patterns("__pycache__"))

    s = Site(root)
    s.write("index.md", "# Test home\n\n[Link](fa99-midterm/index.html)\n")
    s.write("assets/theme.css", "body { color: black; }\n")
    (root / "assets/images/fa99-midterm").mkdir(parents=True)
    (root / "assets/images/fa99-midterm/pic.png").write_bytes(b"not-really-a-png")
    (root / "pdfs").mkdir()
    (root / "pdfs/fa-99-midterm.pdf").write_bytes(b"%PDF-fake")
    s.write("problems/fa99-midterm/q01.md", GOOD_PROBLEM)
    s.write("pages/exams/fa99-midterm.yml", page_yml(["fa99-midterm/q01"]))
    (root / "docs").mkdir()
    return s


def _executable(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    path.chmod(path.stat().st_mode | stat.S_IEXEC)
    return path


@pytest.fixture
def fake_pandoc_dir(tmp_path):
    """A folder with a broken `pandoc` that reports 99.0 and always fails."""
    if os.name == "nt":
        pytest.skip("Fake pandoc scripts are POSIX shell scripts")
    folder = tmp_path / "fake-bin"
    _executable(folder / "pandoc", '#!/bin/sh\n[ "$1" = "--version" ] && echo "pandoc 99.0" && exit 0\nexit 7\n')
    return folder


def stub_pypandoc(tmp_path, script):
    """A fake pypandoc package, put first on PYTHONPATH, whose bundled pandoc is `script`."""
    if os.name == "nt":
        pytest.skip("Fake pandoc scripts are POSIX shell scripts")
    folder = tmp_path / "stub"
    (folder / "pypandoc").mkdir(parents=True)
    (folder / "pypandoc" / "__init__.py").write_text("")
    if script is not None:
        _executable(folder / "pypandoc" / "files" / "pandoc", script)
    return folder


@pytest.fixture
def pt():
    """The module under test. Imported here so each test fails on its own if it's missing."""
    return importlib.import_module("utils.pandoc_tool")
