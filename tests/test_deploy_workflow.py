"""GitHub is about to publish the site on every push, so the workflow's rules are checked here."""
import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO / ".github/workflows"


def workflow():
    return yaml.safe_load((WORKFLOWS / "deploy.yml").read_text(encoding="utf-8"))


def triggers():
    parsed = workflow()
    return parsed.get("on", parsed.get(True))  # YAML reads a bare `on` key as True


def steps(job):
    return workflow()["jobs"][job]["steps"]


def run_commands(job):
    return [step.get("run", "") for step in steps(job)]


def step_using(job, action):
    return next(step for step in steps(job) if action in step.get("uses", ""))


def test_it_is_the_only_workflow():
    assert sorted(path.name for path in WORKFLOWS.iterdir()) == ["deploy.yml"]


def test_runs_on_master_pushes_prs_and_by_hand():
    on = triggers()
    assert "master" in on["push"]["branches"]
    # uv-stage-2 is a temporary test trigger, to be removed before merging.
    assert set(on["push"]["branches"]) <= {"master", "uv-stage-2"}
    assert on["pull_request"]["branches"] == ["master"]
    assert "workflow_dispatch" in on


def test_no_file_list_can_skip_a_build():
    on = triggers()
    for event in ["push", "pull_request"]:
        assert "paths" not in on[event]
        assert "paths-ignore" not in on[event]


def test_builds_with_the_locked_environment():
    commands = run_commands("build")
    assert "uv sync --locked" in commands
    version = step_using("build", "astral-sh/setup-uv")["with"]["version"]
    assert re.fullmatch(r"\d+\.\d+\.\d+", str(version))
    text = (WORKFLOWS / "deploy.yml").read_text(encoding="utf-8")
    assert "apt-get" not in text
    assert "pip install" not in text


def test_tests_run_before_the_build_and_the_build_uploads_docs():
    commands = run_commands("build")
    assert commands.index("uv sync --locked") < commands.index("uv run pytest") < commands.index("uv run run.py")
    names = [step.get("run", step.get("uses", "")) for step in steps("build")]
    upload = next(i for i, name in enumerate(names) if "upload-pages-artifact" in name)
    assert commands.index("uv run run.py") < upload
    assert step_using("build", "upload-pages-artifact")["with"]["path"] == "./docs"


def test_publishing_needs_a_passing_build_on_a_push_to_master():
    deploy = workflow()["jobs"]["deploy"]
    assert deploy["needs"] == "build"
    condition = deploy["if"]
    assert "github.event_name == 'push'" in condition
    assert "github.ref == 'refs/heads/master'" in condition
    assert "&&" in condition
    assert deploy["environment"]["name"] == "github-pages"
    assert step_using("deploy", "actions/deploy-pages")


def test_only_the_deploy_job_can_write_to_pages():
    parsed = workflow()
    assert "write" not in str(parsed.get("permissions", {}))
    assert "write" not in str(parsed["jobs"]["build"]["permissions"])
    assert parsed["jobs"]["deploy"]["permissions"] == {"pages": "write", "id-token": "write"}


def test_newer_pushes_replace_builds_but_never_interrupt_a_publish():
    jobs = workflow()["jobs"]
    assert jobs["build"]["concurrency"]["cancel-in-progress"] is True
    assert jobs["deploy"]["concurrency"]["cancel-in-progress"] is False
    assert jobs["build"]["concurrency"]["group"] != jobs["deploy"]["concurrency"]["group"]


def test_actions_are_pinned_to_versions():
    for job in workflow()["jobs"]:
        for step in steps(job):
            if "uses" in step:
                assert re.search(r"@v\d+", step["uses"]), step["uses"]
