import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.canJump([2, 3, 1, 1, 4])
assert not sol.canJump([3, 2, 1, 0, 4])
assert sol.canJump([0])

print("All tests passed!")
