import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.intToRoman(3749) == "MMMDCCXLIX"
assert sol.intToRoman(58) == "LVIII"
assert sol.intToRoman(1994) == "MCMXCIV"
assert sol.intToRoman(1) == "I"
assert sol.intToRoman(3999) == "MMMCMXCIX"

print("All tests passed!")
