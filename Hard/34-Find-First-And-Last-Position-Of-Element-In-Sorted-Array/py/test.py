import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert sol.searchRange([], 0) == [-1, -1]

print("All tests passed!")
