import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

nums = [1, 1, 1, 2, 2, 3]
k = sol.removeDuplicates(nums)
assert k == 5
assert nums[:k] == [1, 1, 2, 2, 3]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k = sol.removeDuplicates(nums)
assert k == 7
assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]

nums = [1, 1, 1, 1]
k = sol.removeDuplicates(nums)
assert k == 2
assert nums[:k] == [1, 1]

nums = [1]
k = sol.removeDuplicates(nums)
assert k == 1
assert nums[:k] == [1]

nums = [1, 2, 3, 4, 5]
k = sol.removeDuplicates(nums)
assert k == 5
assert nums[:k] == [1, 2, 3, 4, 5]

nums = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
k = sol.removeDuplicates(nums)
assert k == 6
assert nums[:k] == [1, 1, 2, 2, 3, 3]

print("All tests passed!")
