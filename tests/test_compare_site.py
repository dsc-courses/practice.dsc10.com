"""The site comparison must catch every kind of hand edit tutors have made to docs/,
and must not flag harmless differences such as whitespace or new content.

The last test is the real check: set SITE_REFERENCE and SITE_BUILT to two copies of
the site (e.g. docs/ from master and a fresh build) to confirm nothing is lost.
"""
import importlib.util
import os
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("compare_site", REPO / "scripts" / "compare_site.py")
cs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cs)

BASE = """<html><head><link rel="stylesheet" href="../assets/theme.css"></head><body>
<h2 id="problem-1">Problem 1</h2>
<p>What is <code>x</code>?</p>
{extra}
</body></html>"""


def lost(ref_extra, built_extra=""):
    return cs.compare_page(BASE.format(extra=ref_extra), BASE.format(extra=built_extra))


def test_identical_pages_have_nothing_missing():
    assert lost("") == []


def test_whitespace_and_line_wrapping_do_not_count():
    # Pandoc can rewrap lines differently; the words are all still there in order.
    assert lost("<p>The   quick\nbrown fox</p>", "<p>The quick brown\n   fox</p>") == []
    assert lost("<p>The quick brown fox</p>", "<div><p>The quick</p>\n<p>brown fox</p></div>") == []


def test_catches_changed_wording():
    assert ("text", "brown", 1) in lost("<p>The quick brown fox</p>", "<p>The quick red fox</p>")


def test_new_content_in_the_build_is_fine():
    assert lost("", "<p>A brand new explanation.</p>") == []


def test_catches_a_dropped_banner():
    problems = lost('<div class="alert">PDF version available <a href="../pdfs/quiz1_sp24.pdf">here</a></div>')
    kinds = {(k, v) for k, v, _ in problems}
    assert ("text", "PDF version available here") in kinds
    assert ("url", "../pdfs/quiz1_sp24.pdf") in kinds


def test_catches_a_dropped_video():
    problems = lost('<iframe src="https://www.youtube.com/embed/abc123"></iframe>')
    assert ("url", "https://www.youtube.com/embed/abc123", 1) in problems


def test_catches_a_dropped_or_changed_inline_script():
    ref = "<script>var limit = 30 * 60 * 1000; startTimer(limit);</script>"
    assert any(k == "inline-script" for k, _, _ in lost(ref))
    assert any(k == "inline-script" for k, _, _ in lost(ref, ref.replace("30", "50")))
    # Reindenting the same script is fine
    assert lost(ref, "<script>\n  var limit = 30 * 60 * 1000;  startTimer(limit);\n</script>") == []


def test_catches_a_dropped_tracker_hook():
    ref = '<button type="button" class="pt-done" data-problem="fa24-final/q01">Mark done</button>'
    problems = lost(ref, '<button type="button" class="pt-done">Mark done</button>')
    assert ("attr", "button[data-problem=fa24-final/q01]", 1) in problems


def test_catches_one_of_two_repeated_lines_going_missing():
    assert lost("<p>Answer: 5</p><p>Answer: 5</p>", "<p>Answer: 5</p>") == [("text", "Answer: 5", 1)]


def test_catches_text_moved_out_of_place_only_as_missing_once():
    # A banner moved from the top to the bottom is still on the page, but out of
    # order; flag it so a person looks, rather than silently passing.
    assert lost("<p>Banner</p><p>Body text</p>", "<p>Body text</p><p>Banner</p>") == [("text", "Banner", 1)]


def test_site_level_missing_and_changed_files(tmp_path):
    ref, built = tmp_path / "ref", tmp_path / "built"
    for root in (ref, built):
        (root / "pdfs").mkdir(parents=True)
        (root / "a").mkdir()
    (ref / "pdfs/quiz5_fa25.pdf").write_bytes(b"%PDF-1")
    (ref / "pdfs/same.pdf").write_bytes(b"%PDF-same")
    (built / "pdfs/same.pdf").write_bytes(b"%PDF-same")
    (ref / "a/theme.css").write_text("body{}")
    (built / "a/theme.css").write_text("body{color:red}")
    (ref / "a/index.html").write_text(BASE.format(extra=""))
    (built / "a/index.html").write_text(BASE.format(extra="<p>new</p>"))
    (ref / ".DS_Store").write_bytes(b"junk")
    (built / "only-in-build.html").write_text("new page")

    report = cs.compare_sites(ref, built)
    assert set(report) == {"pdfs/quiz5_fa25.pdf", "a/theme.css"}
    assert cs.main(["x", str(ref), str(built)]) == 1
    assert cs.main(["x", str(ref), str(ref)]) == 0


@pytest.mark.skipif(
    not (os.environ.get("SITE_REFERENCE") and os.environ.get("SITE_BUILT")),
    reason="Set SITE_REFERENCE and SITE_BUILT to compare two real copies of the site",
)
def test_build_keeps_everything_on_the_live_site():
    report = cs.compare_sites(os.environ["SITE_REFERENCE"], os.environ["SITE_BUILT"])
    assert not report, cs.format_report(report)


def test_catches_a_dropped_id_on_any_tag():
    # The timer looks up <aside id="timed-timer">; losing the id breaks timer mode.
    problems = lost('<aside id="timed-timer">00:00</aside>', "<aside>00:00</aside>")
    assert ("attr", "aside[id=timed-timer]", 1) in problems


def test_catches_a_dropped_class_that_scripts_select_on():
    # Solution toggles and the progress tracker hook onto classes, not ids.
    ref = '<div class="accordion"><button class="accordion-button pt-done">Show</button></div>'
    problems = lost(ref, '<div class="acc"><button class="accordion-button">Show</button></div>')
    assert ("class", "accordion", 1) in problems
    assert ("class", "pt-done", 1) in problems
    assert lost(ref, ref.replace('class="accordion-button pt-done"', 'class="pt-done  accordion-button"')) == []


def test_catches_lost_alt_text_title_and_banner_styling():
    assert ("attr", "img[alt=A histogram]", 1) in lost('<img src="h.png" alt="A histogram">', '<img src="h.png">')
    style = "background:#e8eaff;border-left:3px solid #4a90d9"
    assert ("attr", f"div[style={style}]", 1) in lost(f'<div style="{style}">Note</div>', "<div>Note</div>")
    assert ("title", "Fall 2024 Final", 1) in cs.compare_page(
        "<html><head><title>Fall 2024 Final</title></head><body></body></html>",
        "<html><head><title> </title></head><body></body></html>",
    )


def test_catches_a_dropped_same_page_link():
    assert ("url", "#problem-1", 1) in lost('<a href="#problem-1">Jump</a>')


def test_catches_a_changed_dropdown_option_and_link_target():
    ref = '<select><option value="done" selected>Done</option></select><a href="x.pdf" target="_blank" aria-expanded="false">PDF</a>'
    problems = lost(ref, '<select><option value="todo">Done</option></select><a href="x.pdf">PDF</a>')
    assert ("attr", "option[value=done]", 1) in problems
    assert ("attr", "option[selected=]", 1) in problems
    assert ("attr", "a[target=_blank]", 1) in problems
    assert ("attr", "a[aria-expanded=false]", 1) in problems
