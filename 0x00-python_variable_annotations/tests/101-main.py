#!/usr/bin/env python3
import importlib.util
import sys
from pathlib import Path

# Define the path to the module
module_path = Path(__file__).resolve().parent.parent / '101-safely_get_value.py'

# Load the module
spec = importlib.util.spec_from_file_location("add_module", module_path)
module = importlib.util.module_from_spec(spec)
sys.modules["add_module"] = module
spec.loader.exec_module(module)

safely_get_value = module.safely_get_value

annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))
