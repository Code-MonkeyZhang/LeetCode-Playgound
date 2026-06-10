import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
assert sol.search([1], 1) == 0

print("All tests passed!")
