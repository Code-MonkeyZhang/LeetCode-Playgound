import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.majorityElement([3, 2, 3]) == 3
assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
assert sol.majorityElement([1]) == 1

print("All tests passed!")
