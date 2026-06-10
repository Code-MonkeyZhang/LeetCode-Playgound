import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
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
