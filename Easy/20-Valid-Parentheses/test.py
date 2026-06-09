import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.isValid("()")
assert sol.isValid("()[]{}")
assert not sol.isValid("(]")
assert not sol.isValid("([)]")
assert sol.isValid("{[]}")
assert sol.isValid("")
assert not sol.isValid("]")
assert not sol.isValid("((")

print("All tests passed!")
