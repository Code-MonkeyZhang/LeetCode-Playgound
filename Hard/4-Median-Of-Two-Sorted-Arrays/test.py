import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert sol.findMedianSortedArrays([1], [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5

print("All tests passed!")
