# LeetCode 1 — 两数之和
#
# 题目描述：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且不能使用同一个元素两次。
#
# 示例 1：输入: nums = [2,7,11,15], target = 9 → 输出: [0,1]
# 示例 2：输入: nums = [3,2,4], target = 6 → 输出: [1,2]
# 示例 3：输入: nums = [3,3], target = 6 → 输出: [0,1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )