import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert len(sol.longestPalindrome("babad")) == 3
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("a") == "a"

print("All tests passed!")
