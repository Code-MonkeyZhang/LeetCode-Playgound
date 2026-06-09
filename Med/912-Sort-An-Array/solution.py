# LeetCode 912 — 排序数组
#
# 题目描述：给你一个整数数组 nums，请你将该数组升序排列。
#
# 示例 1：输入: nums = [5,2,3,1] → 输出: [1,2,3,5]
# 示例 2：输入: nums = [5,1,1,2,0,0] → 输出: [0,0,1,1,2,5]

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)
