import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

nums = [1, 1, 2]
k = sol.removeDuplicates(nums)
assert k == 2
assert nums[:k] == [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)
assert k == 5
assert nums[:k] == [0, 1, 2, 3, 4]

nums = [1]
k = sol.removeDuplicates(nums)
assert k == 1
assert nums[:k] == [1]

nums = [1, 1, 1, 1]
k = sol.removeDuplicates(nums)
assert k == 1
assert nums[:k] == [1]

nums = [1, 2, 3, 4, 5]
k = sol.removeDuplicates(nums)
assert k == 5
assert nums[:k] == [1, 2, 3, 4, 5]

print("All tests passed!")
