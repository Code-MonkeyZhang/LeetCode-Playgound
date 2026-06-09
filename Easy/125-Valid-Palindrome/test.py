import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.isPalindrome("A man, a plan, a canal: Panama")
assert not sol.isPalindrome("race a car")
assert sol.isPalindrome(" ")
assert not sol.isPalindrome("0P")

print("All tests passed!")
