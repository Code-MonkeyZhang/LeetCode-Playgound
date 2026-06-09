import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.reverse(123) == 321
assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21
assert sol.reverse(1534236469) == 0

print("All tests passed!")
