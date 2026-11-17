"""Once the site is published from source, docs/ is build output: a hand edit there
would be overwritten on the next publish. CI must reject any commit that edits it."""
import importlib.util
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "check_docs_untouched.py"


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def repo(tmp_path):
    git(tmp_path, "init", "-q", "-b", "master")
    git(tmp_path, "config", "user.email", "t@example.com")
    git(tmp_path, "config", "user.name", "Tutor")
    (tmp_path / "docs/q1").mkdir(parents=True)
    (tmp_path / "docs/q1/index.html").write_text("<p>old</p>")
    (tmp_path / "problems").mkdir()
    (tmp_path / "problems/q1.md").write_text("old")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-q", "-m", "base")
    return tmp_path


def commit(repo, files, delete=()):
    for rel, text in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    for rel in delete:
        (repo / rel).unlink()
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "change")
    return git(repo, "rev-parse", "HEAD")


def check(repo, base, head):
    return subprocess.run(
        ["python3", str(SCRIPT), base, head], cwd=repo, capture_output=True, text=True
    )


def test_editing_only_markdown_passes(repo):
    base = git(repo, "rev-parse", "HEAD")
    head = commit(repo, {"problems/q1.md": "new wording", "pages/quiz.yml": "title: x"})
    result = check(repo, base, head)
    assert result.returncode == 0, result.stdout + result.stderr


def test_editing_docs_by_hand_fails_and_says_what_to_do(repo):
    base = git(repo, "rev-parse", "HEAD")
    head = commit(repo, {"docs/q1/index.html": "<p>hand edit</p>", "problems/q1.md": "new"})
    result = check(repo, base, head)
    assert result.returncode == 1
    assert "docs/q1/index.html" in result.stdout
    assert "git restore" in result.stdout or "git checkout" in result.stdout
    assert "problems/" in result.stdout


def test_adding_a_file_under_docs_fails(repo):
    base = git(repo, "rev-parse", "HEAD")
    head = commit(repo, {"docs/pdfs/new.pdf": "%PDF"})
    assert check(repo, base, head).returncode == 1


def test_deleting_docs_is_allowed(repo):
    # Removing the old committed build can't hide content from the published site.
    base = git(repo, "rev-parse", "HEAD")
    head = commit(repo, {}, delete=["docs/q1/index.html"])
    assert check(repo, base, head).returncode == 0


def test_only_the_branchs_own_changes_count(repo):
    # A PR whose branch started before someone else's docs/ commit on master
    # isn't blamed for it: the check compares against the merge base.
    base_commit = git(repo, "rev-parse", "HEAD")
    git(repo, "checkout", "-q", "-b", "tutor")
    head = commit(repo, {"problems/q1.md": "tutor edit"})
    git(repo, "checkout", "-q", "master")
    master = commit(repo, {"docs/q1/index.html": "<p>someone else</p>"})
    assert base_commit != master
    assert check(repo, master, head).returncode == 0


def test_a_brand_new_branch_push_with_no_before_commit_is_skipped(repo):
    head = git(repo, "rev-parse", "HEAD")
    result = check(repo, "0" * 40, head)
    assert result.returncode == 0
    assert "skip" in result.stdout.lower()


def test_script_is_importable_without_running():
    spec = importlib.util.spec_from_file_location("check_docs_untouched", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert callable(module.main)
