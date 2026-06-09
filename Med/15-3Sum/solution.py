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
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = num1 + nums[left] + nums[right]
                if threeSum == 0:
                    ans.append([num1, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
        return ans
