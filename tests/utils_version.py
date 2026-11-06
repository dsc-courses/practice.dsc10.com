"""Read the pinned pandoc version for tests that fake a matching binary."""
import importlib


def pinned_version():
    return importlib.import_module("utils.pandoc_tool").PINNED_PANDOC_VERSION
