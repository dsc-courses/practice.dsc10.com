"""The pandoc helper must always use the pinned, bundled pandoc and report failures."""
import os
import subprocess
from pathlib import Path

import pypandoc
import pytest


def test_bundled_path_is_inside_the_pypandoc_package(pt):
    path = Path(pt.bundled_pandoc_path())
    assert path.exists()
    assert Path(pypandoc.__file__).parent in path.parents


def test_real_bundled_version_matches_the_pin(pt):
    pt.check_pandoc_version()
    out = subprocess.run([pt.bundled_pandoc_path(), "--version"], capture_output=True, text=True).stdout
    assert out.splitlines()[0] == f"pandoc {pt.PINNED_PANDOC_VERSION}"


def test_another_pandoc_first_on_path_is_ignored(pt, tmp_path, monkeypatch, fake_pandoc_dir):
    monkeypatch.setenv("PATH", f"{fake_pandoc_dir}{os.pathsep}{os.environ['PATH']}")
    src, dst = tmp_path / "in.md", tmp_path / "out.html"
    src.write_text("hello *world*\n", encoding="utf-8")
    pt.run_pandoc([str(src), "-o", str(dst)], source=str(src))  # The fake would exit 7
    assert "<em>world</em>" in dst.read_text(encoding="utf-8")


def test_works_with_no_pandoc_on_path(pt, tmp_path, monkeypatch):
    monkeypatch.setenv("PATH", str(tmp_path))
    src, dst = tmp_path / "in.md", tmp_path / "out.html"
    src.write_text("hello\n", encoding="utf-8")
    pt.run_pandoc([str(src), "-o", str(dst)], source=str(src))
    assert dst.exists()


def test_wrong_version_gives_clear_error(pt, monkeypatch, fake_pandoc_dir):
    monkeypatch.setattr(pt, "bundled_pandoc_path", lambda: str(fake_pandoc_dir / "pandoc"))
    with pytest.raises(pt.PandocError) as err:
        pt.check_pandoc_version()
    assert pt.PINNED_PANDOC_VERSION in str(err.value)
    assert "99.0" in str(err.value)


def test_missing_binary_says_to_use_uv_run(pt, tmp_path, monkeypatch):
    monkeypatch.setattr(pypandoc, "__file__", str(tmp_path / "pypandoc" / "__init__.py"))
    with pytest.raises(pt.PandocError, match="uv run"):
        pt.bundled_pandoc_path()


def test_pandoc_failure_names_the_source_file(pt, tmp_path):
    missing = tmp_path / "does-not-exist.md"
    with pytest.raises(pt.PandocError, match="problems/fa99/q01.md"):
        pt.run_pandoc([str(missing), "-o", str(tmp_path / "out.html")], source="problems/fa99/q01.md")


def test_warnings_stay_visible_and_do_not_stop_the_build(pt, tmp_path, capfd):
    src, dst = tmp_path / "in.md", tmp_path / "out.html"
    src.write_text("::: {.box}\nnever closed\n", encoding="utf-8")
    pt.run_pandoc([str(src), "-o", str(dst)], source=str(src))
    assert dst.exists()
    assert "unclosed" in capfd.readouterr().err


def test_spaces_and_special_characters_are_not_touched_by_a_shell(pt, tmp_path):
    folder = tmp_path / "folder with spaces"
    folder.mkdir()
    src, dst = folder / "in file.md", folder / "out file.html"
    src.write_text("body\n", encoding="utf-8")
    title = 'Quiz "1" costs $HOME `date` — done'
    pt.run_pandoc(["-s", "--metadata", f"title={title}", str(src), "-o", str(dst)], source=str(src))
    html = dst.read_text(encoding="utf-8")
    assert "$HOME" in html  # A shell would have expanded this
    assert "`date`" in html  # A shell would have run this
    assert "—" in html
