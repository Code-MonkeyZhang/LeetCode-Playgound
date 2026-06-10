# LeetCode 34 — 在排序数组中查找元素的第一个和最后一个位置
#
# 题目描述：给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
# 请你找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
# 示例 1：输入: nums = [5,7,7,8,8,10], target = 8 → 输出: [3,4]
# 示例 2：输入: nums = [5,7,7,8,8,10], target = 6 → 输出: [-1,-1]
# 示例 3：输入: nums = [], target = 0 → 输出: [-1,-1]

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(isLeft: bool) -> int:
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if isLeft:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        left = binarySearch(True)
        right = binarySearch(False)

        return [left, right]

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
