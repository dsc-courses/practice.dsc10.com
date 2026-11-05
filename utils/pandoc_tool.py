"""Runs the exact pandoc version the site is pinned to.

pypandoc_binary bundles a pandoc inside the Python package, but `uv run` doesn't
put it on PATH, and pypandoc.get_pandoc_path() can pick a different pandoc that's
installed on the computer. So this module finds the bundled copy by location.
"""
import os
import subprocess

PINNED_PANDOC_VERSION = "3.9"  # Bundled by pypandoc_binary 1.17; update them together.

USE_UV = "Run the site with uv, for example: uv run run.py"


class PandocError(Exception):
    """Pandoc is missing, is the wrong version, or failed."""


def bundled_pandoc_path():
    """Return the path to the pandoc inside the pypandoc_binary package."""
    try:
        import pypandoc
    except ImportError as err:
        raise PandocError(f"pypandoc_binary isn't installed. {USE_UV}") from err

    name = "pandoc.exe" if os.name == "nt" else "pandoc"
    path = os.path.join(os.path.dirname(os.path.abspath(pypandoc.__file__)), "files", name)
    if not os.path.exists(path):
        raise PandocError(f"The bundled pandoc wasn't found at {path}. {USE_UV}")
    return path


def check_pandoc_version():
    """Stop unless the bundled pandoc is the pinned version."""
    result = subprocess.run(
        [bundled_pandoc_path(), "--version"], capture_output=True, text=True, encoding="utf-8"
    )
    first_line = result.stdout.splitlines()[0] if result.stdout else ""
    found = first_line.removeprefix("pandoc ").strip()
    if result.returncode != 0 or found != PINNED_PANDOC_VERSION:
        raise PandocError(
            f"Expected pandoc {PINNED_PANDOC_VERSION}, but found {found or 'nothing'}. {USE_UV}"
        )


def run_pandoc(args, source):
    """Run the bundled pandoc on an argument list, with no shell.

    Warnings print as usual. If pandoc fails, raises PandocError naming `source`,
    the file a person would need to look at.
    """
    result = subprocess.run([bundled_pandoc_path(), *args])
    if result.returncode != 0:
        raise PandocError(f"pandoc failed with exit code {result.returncode} on {source}")
