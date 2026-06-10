import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
assert sol.maxProfit([1, 2]) == 1
assert sol.maxProfit([2, 1]) == 0
assert sol.maxProfit([2, 4, 1]) == 2
assert sol.maxProfit([3, 3, 3, 3]) == 0

print("All tests passed!")
