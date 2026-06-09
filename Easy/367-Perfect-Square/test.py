import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.isPerfectSquare(16)
assert not sol.isPerfectSquare(14)
assert sol.isPerfectSquare(1)
assert sol.isPerfectSquare(0)
assert sol.isPerfectSquare(9)

print("All tests passed!")
