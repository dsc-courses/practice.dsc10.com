"""The LaTeX converter uses pandoc too, so it needs the bundled copy as well."""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_converts_with_no_pandoc_on_path(tmp_path):
    code = (
        "import importlib.util, sys;"
        f"sys.path.insert(0, {str(REPO / 'utils')!r});"
        f"spec = importlib.util.spec_from_file_location('latex_to_md', {str(REPO / 'utils/latex-to-md.py')!r});"
        "m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m);"
        "print(m.pandoc_tex_to_md(r'\\documentclass{article}\\begin{document}\\textbf{hi}\\end{document}'))"
    )
    empty = tmp_path / "empty"
    empty.mkdir()
    result = subprocess.run(
        [sys.executable, "-c", code], cwd=tmp_path, env={"PATH": str(empty)}, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    assert "**hi**" in result.stdout
