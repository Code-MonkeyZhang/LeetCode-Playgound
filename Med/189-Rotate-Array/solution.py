# LeetCode 189 — 轮转数组
#
# 题目描述：给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
# 示例 1：输入: nums = [1,2,3,4,5,6,7], k = 3 → 输出: [5,6,7,1,2,3,4]
# 示例 2：输入: nums = [-1,-100,3,99], k = 2 → 输出: [3,99,-1,-100]

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        if k > length:
            k = k % length

        def reverse_array(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1

        reverse_array(0, length - 1)
        reverse_array(0, k - 1)
        reverse_array(k, length - 1)
