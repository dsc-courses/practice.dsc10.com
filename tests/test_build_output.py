"""With no pandoc installed at all, the bundled one must build the site correctly."""
from conftest import page_yml

PAGE = "pages/exams/fa99-midterm.yml"


def build_ok(site, *args):
    result = site.run(*args)
    assert result.returncode == 0, result.stdout + result.stderr
    return result


def test_page_has_math_solution_and_image(site):
    build_ok(site, PAGE)
    html = (site.root / "docs/fa99-midterm/index.html").read_text(encoding="utf-8")
    assert 'class="math' in html
    assert "katex@0.16.11" in html
    assert "GOOD-ANSWER-TEXT" in html
    assert "BEGIN SOLUTION" not in html
    assert "pic.png" in html
    assert (site.root / "docs/assets/images/fa99-midterm/pic.png").exists()


def test_hidden_solutions_stay_off_the_page(site):
    site.write(PAGE, page_yml(["fa99-midterm/q01"], show_solution=False))
    build_ok(site, PAGE)
    html = (site.root / "docs/fa99-midterm/index.html").read_text(encoding="utf-8")
    assert "GOOD-ANSWER-TEXT" not in html


def test_single_page_build_leaves_everything_else_alone(site):
    other = site.write("docs/other/index.html", "other page")
    build_ok(site, PAGE)
    assert other.read_text() == "other page"
    assert not (site.root / "docs/lectures").exists()
    assert not (site.root / "docs/index.html").exists()
    assert not (site.root / "docs/fa99-midterm.md").exists()


def test_full_build_writes_the_whole_site(site):
    stale = site.write("docs/stale/index.html", "old")
    build_ok(site)
    docs = site.root / "docs"
    assert (docs / "CNAME").read_text() == "practice.dsc10.com"
    assert (docs / "index.html").exists()
    assert (docs / "fa99-midterm/index.html").exists()
    assert (docs / "assets/theme.css").exists()
    assert (docs / "pdfs/fa-99-midterm.pdf").exists()
    assert "GOOD-ANSWER-TEXT" in (docs / "lectures/lec1/index.html").read_text(encoding="utf-8")
    assert not stale.exists()
    assert not (site.root / "temp").exists()
    assert list(docs.glob("*.md")) == []


def test_two_full_builds_are_byte_identical(site):
    build_ok(site)
    docs = site.root / "docs"
    first = {p.relative_to(docs): p.read_bytes() for p in docs.rglob("*") if p.is_file()}
    build_ok(site)
    second = {p.relative_to(docs): p.read_bytes() for p in docs.rglob("*") if p.is_file()}
    assert first == second
