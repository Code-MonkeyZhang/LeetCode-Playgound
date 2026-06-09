import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

nums = [3, 2, 2, 3]
k = sol.removeElement(nums, 3)
assert k == 2
assert sorted(nums[:k]) == [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = sol.removeElement(nums, 2)
assert k == 5
assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

nums = []
k = sol.removeElement(nums, 0)
assert k == 0

nums = [1, 1, 1]
k = sol.removeElement(nums, 1)
assert k == 0

nums = [2, 3, 4]
k = sol.removeElement(nums, 1)
assert k == 3
assert sorted(nums[:k]) == [2, 3, 4]

print("All tests passed!")
