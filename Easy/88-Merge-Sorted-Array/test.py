import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

nums1 = [1, 2, 3, 0, 0, 0]
sol.merge(nums1, 3, [2, 5, 6], 3)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1 = [1]
sol.merge(nums1, 1, [], 0)
assert nums1 == [1]

nums1 = [0]
sol.merge(nums1, 0, [1], 1)
assert nums1 == [1]

nums1 = [2, 0]
sol.merge(nums1, 1, [1], 1)
assert nums1 == [1, 2]

nums1 = [4, 5, 6, 0, 0, 0]
sol.merge(nums1, 3, [1, 2, 3], 3)
assert nums1 == [1, 2, 3, 4, 5, 6]

print("All tests passed!")
