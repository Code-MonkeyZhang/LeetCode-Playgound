import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, 3)
assert nums == [5, 6, 7, 1, 2, 3, 4]

nums = [-1, -100, 3, 99]
sol.rotate(nums, 2)
assert nums == [3, 99, -1, -100]

nums = [1]
sol.rotate(nums, 0)
assert nums == [1]

nums = [1, 2]
sol.rotate(nums, 1)
assert nums == [2, 1]

nums = [1, 2, 3]
sol.rotate(nums, 4)
assert nums == [3, 1, 2]

nums = [1, 2, 3, 4, 5, 6]
sol.rotate(nums, 6)
assert nums == [1, 2, 3, 4, 5, 6]

print("All tests passed!")
