import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
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
