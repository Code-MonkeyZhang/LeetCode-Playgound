# LeetCode 15 — 三数之和
#
# 题目描述：给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]]
# 满足 i != j、i != k 且 j != k，同时还满足 nums[i] + nums[j] + nums[k] == 0。
# 请你返回所有和为 0 且不重复的三元组。
#
# 示例 1：输入: nums = [-1,0,1,2,-1,-4] → 输出: [[-1,-1,2],[-1,0,1]]
# 示例 2：输入: nums = [0,1,1] → 输出: []
# 示例 3：输入: nums = [0,0,0] → 输出: [[0,0,0]]


class Solution:
    def threeSum(self, nums):
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
