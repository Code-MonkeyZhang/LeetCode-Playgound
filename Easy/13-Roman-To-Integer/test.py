import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.romanToInt("III") == 3
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
assert sol.romanToInt("I") == 1
assert sol.romanToInt("MMMDCCXLIX") == 3749

print("All tests passed!")
