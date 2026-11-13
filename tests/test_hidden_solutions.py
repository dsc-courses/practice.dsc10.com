"""Once every push publishes, a hidden page must not leak through lecture pages."""
from conftest import GOOD_PROBLEM, TAGGED_MISSING_SOLUTION, page_yml

EXAM = "pages/exams/fa99-midterm.yml"
ANSWER = "GOOD-ANSWER-TEXT"
OTHER_ANSWER = "OTHER-ANSWER-TEXT"
HIDDEN_QUESTION = "What is"
LECTURE = "docs/lectures/lec1/index.html"


def full_build(site):
    result = site.run()
    assert result.returncode == 0, result.stdout + result.stderr


def read(site, relative):
    return (site.root / relative).read_text(encoding="utf-8")


def add_visible_page_for_lecture_1(site):
    """A second, visible page, so lecture 1's page still exists when the other is hidden."""
    text = GOOD_PROBLEM.replace(ANSWER, OTHER_ANSWER).replace("What is", "Compute")
    site.write("problems/fa99-final/q01.md", text)
    site.write("pages/exams/fa99-final.yml", page_yml(["fa99-final/q01"]))


def test_hidden_exam_stays_off_lecture_pages(site):
    add_visible_page_for_lecture_1(site)
    site.write(EXAM, page_yml(["fa99-midterm/q01"], show_solution=False))
    full_build(site)
    lecture = read(site, LECTURE)
    assert OTHER_ANSWER in lecture  # The lecture page itself still builds
    assert ANSWER not in lecture
    assert HIDDEN_QUESTION not in lecture
    assert ANSWER not in read(site, "docs/fa99-midterm/index.html")


def test_hidden_quiz_stays_off_lecture_pages(site):
    add_visible_page_for_lecture_1(site)
    site.write("problems/fa99-quizzes/quiz1/q01.md", GOOD_PROBLEM)
    site.write("pages/quizzes/fa99-quiz1.yml", page_yml(["fa99-quizzes/quiz1/q01"], show_solution=False))
    site.write(EXAM, page_yml(["fa99-final/q01"]))
    full_build(site)
    lecture = read(site, LECTURE)
    assert OTHER_ANSWER in lecture
    assert ANSWER not in lecture


def test_hidden_discussion_1_stays_off_lecture_pages(site):
    add_visible_page_for_lecture_1(site)
    site.write(EXAM, page_yml(["fa99-final/q01"]))
    site.write("problems/disc/disc01-test.md", GOOD_PROBLEM)
    site.write("pages/disc/disc01.yml", page_yml(["disc/disc01-test"], show_solution=False))
    full_build(site)
    lecture = read(site, LECTURE)
    assert OTHER_ANSWER in lecture
    assert ANSWER not in lecture


def test_problem_on_hidden_and_visible_pages_is_credited_to_the_visible_one(site):
    # fa98 sorts first, so without the fix the hidden page gets the credit.
    site.write("pages/exams/fa98-midterm.yml", page_yml(["fa99-midterm/q01"], show_solution=False))
    full_build(site)
    lecture = read(site, LECTURE)
    assert lecture.count(ANSWER) == 1
    assert "fa99-midterm/index.html#problem-1" in lecture
    assert "fa98-midterm" not in lecture


def test_lecture_with_only_hidden_problems_is_not_built_or_linked(site):
    site.write(EXAM, page_yml(["fa99-midterm/q01"], show_solution=False))
    full_build(site)
    assert not (site.root / LECTURE).exists()
    assert "lectures/lec1" not in read(site, "docs/index.html")


def test_visible_page_appears_on_lecture_page_and_homepage(site):
    full_build(site)
    assert ANSWER in read(site, LECTURE)
    assert "lectures/lec1" in read(site, "docs/index.html")


def test_missing_setting_counts_as_visible(site):
    # pages/exams/fa24-final.yml has no show_solution line, and it must keep appearing.
    site.write(EXAM, 'title: "T"\ninstructors: "I"\ncontext: "C"\nproblems:\n  - fa99-midterm/q01\n')
    full_build(site)
    assert ANSWER in read(site, LECTURE)


def test_changing_hidden_to_visible_releases_the_solutions(site):
    site.write(EXAM, page_yml(["fa99-midterm/q01"], show_solution=False))
    full_build(site)
    site.write(EXAM, page_yml(["fa99-midterm/q01"], show_solution=True))
    full_build(site)
    assert ANSWER in read(site, "docs/fa99-midterm/index.html")
    assert ANSWER in read(site, LECTURE)


def test_hidden_page_can_have_no_solutions_written_yet(site):
    site.write("problems/fa99-midterm/q01.md", TAGGED_MISSING_SOLUTION)
    site.write(EXAM, page_yml(["fa99-midterm/q01"], show_solution=False))
    full_build(site)
