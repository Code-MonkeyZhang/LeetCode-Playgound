import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
assert sol.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]

print("All tests passed!")
