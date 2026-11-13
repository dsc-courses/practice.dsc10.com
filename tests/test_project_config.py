"""The uv setup must be complete, and the old setup instructions must be gone."""
import shutil
import subprocess
import tomllib
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORKFLOW = REPO / ".github/workflows/pages-preview.yml"


def test_lockfile_matches_pyproject():
    uv = shutil.which("uv")
    assert uv, "uv must be installed to run this test"
    result = subprocess.run([uv, "lock", "--check"], cwd=REPO, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_pandoc_and_python_are_pinned():
    project = tomllib.loads((REPO / "pyproject.toml").read_text())["project"]
    assert "pypandoc_binary==1.17" in project["dependencies"]
    assert project["requires-python"] == "==3.11.*"
    assert (REPO / ".python-version").read_text().strip() == "3.11"


def test_requirements_file_is_gone():
    assert not (REPO / "requirements.txt").exists()


def test_readme_describes_the_uv_setup():
    readme = (REPO / "README.md").read_text(encoding="utf-8")
    assert "uv run run.py" in readme
    assert "pip install" not in readme
    assert "standalone program" not in readme
    assert "# BEGIN SOLUTION" in readme  # The style guide must survive


def test_ci_uses_the_locked_environment():
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "uv sync --locked" in workflow
    assert "uv run run.py" in workflow
    assert "uv run pytest" in workflow
    assert "apt-get install" not in workflow
    assert "requirements.txt" not in workflow


def test_ci_cannot_deploy_to_pages():
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "deploy-pages" not in workflow
    assert "pages: write" not in workflow
