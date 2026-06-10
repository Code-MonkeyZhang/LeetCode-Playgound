import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0

print("All tests passed!")
