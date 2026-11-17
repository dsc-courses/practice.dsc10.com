"""The everyday tutor edits, made only in source files, must show up correctly on the
published site, which CI builds with a full `uv run run.py`.

Each test starts from a published site, makes one kind of edit the way a tutor
would (problems/, pages/, index.md, assets/, pdfs/ only, never docs/), rebuilds
like CI does, and checks the rendered pages, including the lecture pages and
homepage data that a one-page preview doesn't refresh.
"""
import json

from conftest import GOOD_PROBLEM, page_yml

EXAM_YML = "pages/exams/fa99-midterm.yml"
EXAM = "docs/fa99-midterm/index.html"
LECTURE = "docs/lectures/lec1/index.html"
HOME = "docs/index.html"


def publish(site):
    """What CI does on every push."""
    result = site.run()
    assert result.returncode == 0, result.stdout + result.stderr


def read(site, relative):
    return (site.root / relative).read_text(encoding="utf-8")


def edit(site, relative, old, new):
    path = site.root / relative
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {relative}"
    path.write_text(text.replace(old, new), encoding="utf-8")


def test_fixing_a_typo_in_a_problem_updates_its_page_and_lecture_page(site):
    publish(site)
    edit(site, "problems/fa99-midterm/q01.md", "What is $x^2$", "Find the value of $x^2$")
    publish(site)
    for page in (EXAM, LECTURE):
        html = read(site, page)
        assert "Find the value of" in html
        assert "What is" not in html


def test_editing_a_solution_updates_the_solution_box_everywhere(site):
    publish(site)
    edit(site, "problems/fa99-midterm/q01.md", "GOOD-ANSWER-TEXT", "FIXED-ANSWER-TEXT")
    publish(site)
    for page in (EXAM, LECTURE):
        html = read(site, page)
        assert "FIXED-ANSWER-TEXT" in html
        assert "GOOD-ANSWER-TEXT" not in html
        assert 'class="accordion' in html  # still inside a click-to-show solution


def test_adding_an_explanation_video_link_renders_it(site):
    publish(site)
    edit(
        site,
        "problems/fa99-midterm/q01.md",
        "<average>61</average>",
        "<average>61</average>\n\n🎥 [Walkthrough video](https://podcast.ucsd.edu/watch/fa99/dsc10/1#1:42)",
    )
    publish(site)
    for page in (EXAM, LECTURE):
        assert 'href="https://podcast.ucsd.edu/watch/fa99/dsc10/1#1:42"' in read(site, page)


def test_adding_a_problem_to_a_page_adds_it_everywhere_it_belongs(site):
    publish(site)
    site.write("problems/fa99-midterm/q02.md", GOOD_PROBLEM.replace("GOOD-ANSWER-TEXT", "SECOND-ANSWER").replace("What is", "Now find"))
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01", "fa99-midterm/q02"]))
    publish(site)

    exam = read(site, EXAM)
    assert 'data-src="fa99-midterm/q02" id="problem-2"' in exam
    assert "SECOND-ANSWER" in exam
    assert "SECOND-ANSWER" in read(site, LECTURE)  # tagged lecture: 1 in its front matter
    totals = json.loads(read(site, "docs/assets/exam-totals.json"))
    assert totals["fa99-midterm"]["problems"] == ["fa99-midterm/q01", "fa99-midterm/q02"]
    lectures = json.loads(read(site, "docs/assets/lecture-totals.json"))
    assert lectures["1"] == ["fa99-midterm/q01", "fa99-midterm/q02"]


def test_removing_a_problem_from_a_page_removes_it_everywhere(site):
    site.write("problems/fa99-midterm/q02.md", GOOD_PROBLEM.replace("GOOD-ANSWER-TEXT", "SECOND-ANSWER"))
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01", "fa99-midterm/q02"]))
    publish(site)
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01"]))
    publish(site)
    assert "SECOND-ANSWER" not in read(site, EXAM)
    assert "SECOND-ANSWER" not in read(site, LECTURE)
    assert json.loads(read(site, "docs/assets/exam-totals.json"))["fa99-midterm"]["problems"] == ["fa99-midterm/q01"]
    assert json.loads(read(site, "docs/assets/lecture-totals.json"))["1"] == ["fa99-midterm/q01"]


def test_adding_a_new_quiz_page_with_a_pdf_banner(site):
    publish(site)
    site.write("problems/fa99-quizzes/quiz1/q01.md", GOOD_PROBLEM.replace("GOOD-ANSWER-TEXT", "QUIZ-ANSWER"))
    (site.root / "pdfs/quiz1_fa99.pdf").write_bytes(b"%PDF-quiz")
    banner = (
        '<div style="background:#e8eaff;border-left:3px solid #4a90d9;">\n'
        '⚠️ <strong>PDF version available <a href="../pdfs/quiz1_fa99.pdf">here</a> </strong>.\n'
        "</div>"
    )
    yml = page_yml(["fa99-quizzes/quiz1/q01"], title="Fall 2099 Quiz 1").replace(
        'context: "Test context."',
        "context: |\n  Students had **20 minutes** to work on the quiz.\n\n  " + banner.replace("\n", "\n  "),
    )
    site.write("pages/quizzes/fa99-quiz1.yml", yml)
    edit(site, "index.md", "[Link](fa99-midterm/index.html)", "[Link](fa99-midterm/index.html)\n\n[Quiz 1](fa99-quiz1/index.html)")
    publish(site)

    quiz = read(site, "docs/fa99-quiz1/index.html")
    assert "QUIZ-ANSWER" in quiz
    assert "PDF version available" in quiz
    assert 'href="../pdfs/quiz1_fa99.pdf"' in quiz
    assert (site.root / "docs/pdfs/quiz1_fa99.pdf").read_bytes() == b"%PDF-quiz"
    assert "var limit = 20 * 60 * 1000;" in quiz  # timer mode at the real time limit
    assert 'href="fa99-quiz1/index.html"' in read(site, HOME)
    assert "QUIZ-ANSWER" in read(site, LECTURE)
    assert "fa99-quiz1" in json.loads(read(site, "docs/assets/exam-totals.json"))


def test_adding_an_image_shows_it(site):
    publish(site)
    (site.root / "assets/images/fa99-midterm/new-plot.png").write_bytes(b"new-png")
    edit(site, "problems/fa99-midterm/q01.md", "![A picture]", "![A new plot](../assets/images/fa99-midterm/new-plot.png)\n\n![A picture]")
    publish(site)
    assert "new-plot.png" in read(site, EXAM)
    assert (site.root / "docs/assets/images/fa99-midterm/new-plot.png").read_bytes() == b"new-png"


def test_editing_the_homepage(site):
    publish(site)
    edit(site, "index.md", "# Test home", "# Test home\n\n**🆕 New practice quizzes are up!**")
    publish(site)
    assert "New practice quizzes are up!" in read(site, HOME)


def test_releasing_solutions_by_flipping_show_solution(site):
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01"], show_solution=False))
    publish(site)
    assert "GOOD-ANSWER-TEXT" not in read(site, EXAM)
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01"], show_solution=True))
    publish(site)
    assert "GOOD-ANSWER-TEXT" in read(site, EXAM)
    assert "GOOD-ANSWER-TEXT" in read(site, LECTURE)


def test_a_bad_edit_fails_the_build_and_names_the_file(site):
    publish(site)
    edit(site, "problems/fa99-midterm/q01.md", "# END SOLUTION", "")
    result = site.run()
    assert result.returncode != 0
    assert "fa99-midterm/q01" in result.stdout + result.stderr


def test_retagging_a_problem_moves_it_to_another_lecture_page(site):
    site.write("problems/fa99-midterm/q02.md", GOOD_PROBLEM.replace("GOOD-ANSWER-TEXT", "MOVING-ANSWER"))
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01", "fa99-midterm/q02"]))
    publish(site)
    assert "MOVING-ANSWER" in read(site, LECTURE)
    assert not (site.root / "docs/lectures/lec2").exists()

    edit(site, "problems/fa99-midterm/q02.md", "lecture: 1", "lecture: 2")
    publish(site)
    assert "MOVING-ANSWER" not in read(site, LECTURE)
    assert "MOVING-ANSWER" in read(site, "docs/lectures/lec2/index.html")
    lectures = json.loads(read(site, "docs/assets/lecture-totals.json"))
    assert lectures == {"1": ["fa99-midterm/q01"], "2": ["fa99-midterm/q02"]}
    assert "lectures/lec2/index.html" in read(site, HOME)  # the new lecture gets a homepage button


def test_adding_a_discussion_page(site):
    publish(site)
    site.write("pages/disc/disc01.yml", page_yml(["fa99-midterm/q01"], title="Discussion 1"))
    edit(site, "index.md", "[Link](fa99-midterm/index.html)", "[Link](fa99-midterm/index.html)\n\n[Discussion 1](disc01/index.html)")
    publish(site)
    disc = read(site, "docs/disc01/index.html")
    assert "GOOD-ANSWER-TEXT" in disc
    assert 'data-src="fa99-midterm/q01"' in disc
    assert "timed-start" not in disc  # timer mode is only for quizzes and exams
    assert 'href="disc01/index.html"' in read(site, HOME)


MULTIPART = """---
lecture: 1
---

# BEGIN PROB

A problem with parts.

# BEGIN SUBPROB

Part one asks PART-ONE-QUESTION.

# BEGIN SOLUTION

**Answer**: PART-ONE-ANSWER

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Part two asks PART-TWO-QUESTION.

# BEGIN SOLUTION

**Answer**: PART-TWO-ANSWER

# END SOLUTION

# END SUBPROB

# END PROB
"""


def test_editing_one_part_of_a_multipart_problem(site):
    site.write("problems/fa99-midterm/q02.md", MULTIPART)
    site.write(EXAM_YML, page_yml(["fa99-midterm/q01", "fa99-midterm/q02"]))
    publish(site)
    edit(site, "problems/fa99-midterm/q02.md", "PART-TWO-ANSWER", "PART-TWO-FIXED")
    publish(site)
    for page in (EXAM, LECTURE):
        html = read(site, page)
        assert "PART-ONE-ANSWER" in html and "PART-TWO-FIXED" in html
        assert "PART-TWO-ANSWER" not in html
    exam = read(site, EXAM)
    assert 'id="problem-2.1"' in exam and 'id="problem-2.2"' in exam
    assert exam.count('class="accordion-button"') == 3  # one solution toggle per part, plus q01
