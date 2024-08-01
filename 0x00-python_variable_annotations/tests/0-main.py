# task/tests/0-main.py

import importlib.util
import sys
from pathlib import Path

# Define the path to the module
module_path = Path(__file__).resolve().parent.parent / '0-add.py'

# Load the module
spec = importlib.util.spec_from_file_location("add_module", module_path)
module = importlib.util.module_from_spec(spec)
sys.modules["add_module"] = module
spec.loader.exec_module(module)

# Now you can use the add function from the dynamically imported module
add = module.add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
