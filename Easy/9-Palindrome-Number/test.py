import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.isPalindrome(121)
assert not sol.isPalindrome(-121)
assert not sol.isPalindrome(10)
assert sol.isPalindrome(0)
assert sol.isPalindrome(12321)
assert not sol.isPalindrome(1000021)

print("All tests passed!")
