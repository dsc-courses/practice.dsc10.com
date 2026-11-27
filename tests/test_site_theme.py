"""Theme is automatic: tutors keep authoring ordinary Markdown and YAML."""
import subprocess
import sys
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
import pytest

from conftest import REPO, page_yml


def check_theme(path):
    soup = BeautifulSoup(path.read_text(), 'lxml')
    assert len(soup.select('.site-theme-controls')) == 1
    assert soup.select_one('[data-theme-choice="light"]')['aria-pressed'] == 'true'
    script = soup.head.select_one('script[src$="site-theme.js"]')
    style = soup.head.select_one('link[href$="site-theme.css"]')
    assert script and style
    for el, attr in ((script, 'src'), (style, 'href')):
        target = path.parent / urlsplit(el[attr]).path
        assert target.read_bytes() == (REPO / 'assets' / target.name).read_bytes()


@pytest.mark.parametrize('full_build', [False, True])
def test_shared_theme_without_page_settings(site, full_build):
    page = 'pages/exams/fa99-midterm.yml'
    result = site.run(*([] if full_build else [page]))
    assert result.returncode == 0, result.stdout + result.stderr
    docs = site.root / 'docs'
    check_theme(docs / 'fa99-midterm/index.html')
    if full_build:
        for other in ('index.html', 'lectures/lec1/index.html'):
            check_theme(docs / other)


def test_new_page_and_markdown_edits_keep_theme(site):
    site.write('pages/quizzes/fa99-quiz1.yml', page_yml(['fa99-midterm/q01']))
    question = site.root / 'problems/fa99-midterm/q01.md'
    question.write_text(question.read_text().replace('GOOD-ANSWER-TEXT', 'TUTOR-UPDATED-ANSWER'))
    result = site.run()
    assert result.returncode == 0, result.stdout + result.stderr
    for page in ('fa99-midterm', 'fa99-quiz1', 'lectures/lec1'):
        output = site.root / 'docs' / page / 'index.html'
        check_theme(output)
        assert 'TUTOR-UPDATED-ANSWER' in output.read_text()


def test_page_without_navigation_still_has_theme(site):
    page = 'pages/exams/fa99-midterm.yml'
    site.write(page, page_yml(['fa99-midterm/q01']) + '\nnav: false\n')
    result = site.run(page)
    assert result.returncode == 0, result.stdout + result.stderr
    check_theme(site.root / 'docs/fa99-midterm/index.html')


def test_homepage_only_build_has_theme(site):
    result = site.run('index')
    assert result.returncode == 0, result.stdout + result.stderr
    check_theme(site.root / 'docs/index.html')


def test_listen_mode_update_keeps_theme_and_edits(site):
    page = 'pages/exams/fa99-midterm.yml'
    assert site.run(page).returncode == 0
    question = site.root / 'problems/fa99-midterm/q01.md'
    question.write_text(question.read_text().replace('GOOD-ANSWER-TEXT', 'LISTEN-UPDATED-ANSWER'))
    result = subprocess.run(
        [sys.executable, '-c', f'import run; run.update_page({page!r})'],
        cwd=site.root, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    output = site.root / 'docs/fa99-midterm/index.html'
    check_theme(output)
    assert 'LISTEN-UPDATED-ANSWER' in output.read_text()
