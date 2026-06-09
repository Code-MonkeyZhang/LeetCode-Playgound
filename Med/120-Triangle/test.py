import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
assert sol.minimumTotal(triangle) == 11

triangle = [[-10]]
assert sol.minimumTotal(triangle) == -10

triangle = [[1], [2, 3]]
assert sol.minimumTotal(triangle) == 3

triangle = [[-1], [2, 3], [1, -1, -3]]
assert sol.minimumTotal(triangle) == -1

triangle = [[10], [9, 8], [7, 6, 5], [4, 3, 2, 1]]
assert sol.minimumTotal(triangle) == 24

print("All tests passed!")
