"""Unchecked shell calls are how pandoc failures went unnoticed, so none may remain."""
import ast
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]


def shell_calls(path):
    found = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            if (func.value.id, func.attr) in {("os", "system"), ("os", "popen")}:
                found.append(f"{path.name}:{node.lineno} os.{func.attr}")
        for keyword in node.keywords:
            if keyword.arg == "shell" and getattr(keyword.value, "value", None) is True:
                found.append(f"{path.name}:{node.lineno} shell=True")
    return found


@pytest.mark.parametrize("name", ["run.py", "utils/latex-to-md.py", "utils/pandoc_tool.py"])
def test_no_shell_calls(name):
    path = REPO / name
    assert path.exists(), f"{name} should exist"
    assert shell_calls(path) == []
