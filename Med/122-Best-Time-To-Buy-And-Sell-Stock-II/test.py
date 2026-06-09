import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
assert sol.maxProfit([1]) == 0
assert sol.maxProfit([1, 2]) == 1
assert sol.maxProfit([2, 4, 1]) == 2

print("All tests passed!")
