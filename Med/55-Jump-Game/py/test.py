import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.canJump([2, 3, 1, 1, 4])
assert not sol.canJump([3, 2, 1, 0, 4])
assert sol.canJump([0])

print("All tests passed!")
