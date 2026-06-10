import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"
spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()


def check(result, expected, label):
    assert result == expected, f"{label}: expected {expected}, got {result}"
    assert result[0] < result[1], f"{label}: indices not in ascending order: {result}"


check(sol.twoSum([2, 7, 11, 15], 9), [0, 1], "Example 1")
check(sol.twoSum([3, 2, 4], 6), [1, 2], "Example 2")
check(sol.twoSum([3, 3], 6), [0, 1], "Example 3")
check(sol.twoSum([1, 2], 3), [0, 1], "Min input")
check(sol.twoSum([-1, -2, -3, -4, -5], -8), [2, 4], "All negative")
check(sol.twoSum([-3, 4, 3, 90], 0), [0, 2], "Mixed pos/neg")
check(sol.twoSum([1, 2, 3, 9], 10), [0, 3], "First & last")
check(sol.twoSum([1, 2, 3], 3), [0, 1], "Adjacent pair")
check(sol.twoSum([10, 20, 30, 40, 50], 90), [3, 4], "Last two")
check(sol.twoSum([0, 4, 3, 0], 0), [0, 3], "Contains zero")

print("All tests passed!")
