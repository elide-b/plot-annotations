import glob
import os
from pathlib import Path
import importlib.util

import pytest


@pytest.mark.parametrize(
    "example", glob.glob(str(Path(__file__).parent.parent / "examples" / "*.py"))
)
def test_example_runnable(example):
    # Load the example file as the starbars.__tests__.{name} module
    name = example.split(os.sep)[-1].split(".")[0]
    modname = f"starbars.__tests__.{name}"
    spec = importlib.util.spec_from_file_location(modname, example)
    module = importlib.util.module_from_spec(spec)

    # Execute the example file
    spec.loader.exec_module(module)
