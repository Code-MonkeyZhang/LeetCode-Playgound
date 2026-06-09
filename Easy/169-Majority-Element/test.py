import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.majorityElement([3, 2, 3]) == 3
assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
assert sol.majorityElement([1]) == 1

print("All tests passed!")
