import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert len(sol.longestPalindrome("babad")) == 3
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("a") == "a"

print("All tests passed!")
