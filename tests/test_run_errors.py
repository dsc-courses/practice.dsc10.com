"""When the build can't succeed, run.py must stop, explain why, and protect docs/."""
import pytest

from conftest import MISMATCHED_TAGS, MISSING_SOLUTION, page_yml, stub_pypandoc

PAGE = "pages/exams/fa99-midterm.yml"
BAD = "problems/fa99-midterm/q01.md"


def combined(result):
    return (result.stdout + result.stderr).replace("\\", "/")  # Same paths on Windows


def test_running_without_the_uv_environment_explains_what_to_do(site, tmp_path):
    stub = tmp_path / "no-packages"
    stub.mkdir()
    for module in ["yaml", "pypandoc"]:
        (stub / f"{module}.py").write_text("raise ModuleNotFoundError(f'No module named {__name__!r}', name=__name__)\n")
    result = site.run(PAGE, pythonpath=stub)
    assert result.returncode != 0
    assert "uv run run.py" in combined(result)
    assert "Traceback" not in combined(result)


def test_missing_solution_names_the_problem_file(site):
    site.write(BAD, MISSING_SOLUTION)
    result = site.run(PAGE)
    assert result.returncode != 0
    assert "fa99-midterm/q01.md" in combined(result)
    assert "BEGIN SOLUTION" in combined(result)


def test_mismatched_tags_name_the_problem_file(site):
    site.write(BAD, MISMATCHED_TAGS)
    result = site.run(PAGE)
    assert result.returncode != 0
    assert "fa99-midterm/q01.md" in combined(result)


def test_bad_problem_reached_through_a_lecture_page_names_the_file(site, monkeypatch):
    # Pages build before lecture pages, so call the lecture step directly to reach this path.
    import run

    item = {"path": BAD, "page": "fa99-midterm", "title": "T", "q": 1, "body": MISSING_SOLUTION, "avg": None, "term": 0}
    monkeypatch.chdir(site.root)
    monkeypatch.setattr(run, "collect_problems_by_lecture", lambda: {1: [item]})
    with pytest.raises(run.ProblemError, match="fa99-midterm/q01.md"):
        run.write_lecture_pages()


def test_wrong_pandoc_version_stops_before_docs_is_deleted(site, tmp_path):
    keep = site.write("docs/keep.html", "existing page")
    stub = stub_pypandoc(tmp_path, '#!/bin/sh\necho "pandoc 99.0"\n')
    result = site.run(pythonpath=stub)
    assert result.returncode != 0
    assert "99.0" in combined(result)
    assert keep.exists()


def test_missing_bundled_pandoc_stops_before_docs_is_deleted(site, tmp_path):
    keep = site.write("docs/keep.html", "existing page")
    stub = stub_pypandoc(tmp_path, None)
    result = site.run(pythonpath=stub)
    assert result.returncode != 0
    assert "uv run" in combined(result)
    assert keep.exists()


def test_full_build_failing_partway_gives_recovery_hint(site):
    site.write(BAD, MISSING_SOLUTION)
    result = site.run()
    assert result.returncode != 0
    assert "git restore docs" in combined(result)


def test_single_page_failure_does_not_suggest_restoring_docs(site):
    site.write(BAD, MISSING_SOLUTION)
    assert "git restore docs" not in combined(site.run(PAGE))


def test_problem_listed_but_not_on_disk_fails_and_names_it(site):
    site.write(PAGE, page_yml(["fa99-midterm/q99"]))
    result = site.run()
    assert result.returncode != 0
    assert "q99" in combined(result)
    assert "git restore docs" in combined(result)


def test_pandoc_failing_during_a_build_stops_it_and_names_the_page(site, tmp_path):
    from utils_version import pinned_version

    script = f'#!/bin/sh\n[ "$1" = "--version" ] && echo "pandoc {pinned_version()}" && exit 0\nexit 3\n'
    stub = stub_pypandoc(tmp_path, script)
    result = site.run(PAGE, pythonpath=stub)
    assert result.returncode != 0
    assert "fa99-midterm" in combined(result)
    assert "Traceback" not in combined(result)
