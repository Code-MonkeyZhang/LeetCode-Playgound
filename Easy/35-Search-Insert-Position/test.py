import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.searchInsert([1, 3, 5, 6], 5) == 2
assert sol.searchInsert([1, 3, 5, 6], 2) == 1
assert sol.searchInsert([1, 3, 5, 6], 7) == 4
assert sol.searchInsert([1, 3, 5, 6], 0) == 0
assert sol.searchInsert([1], 0) == 0
assert sol.searchInsert([1], 2) == 1
assert sol.searchInsert([1], 1) == 0

print("All tests passed!")
