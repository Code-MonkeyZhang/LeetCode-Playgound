# LeetCode 4 — 寻找两个正序数组的中位数
#
# 题目描述：给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出并返回这两个正序数组的中位数。算法的时间复杂度应该为 O(log(m+n))。
#
# 示例 1：输入: nums1 = [1,3], nums2 = [2] → 输出: 2.00000（合并数组 = [1,2,3]，中位数 2）
# 示例 2：输入: nums1 = [1,2], nums2 = [3,4] → 输出: 2.50000（合并数组 = [1,2,3,4]，中位数 (2+3)/2 = 2.5）

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        total_length = len_nums1 + len_nums2
        start = 0
        end = len_nums1
        cut_x = (start + end) // 2

        while start <= end:
            cut_y = (total_length + 1) // 2 - cut_x

            if cut_x == 0:
                max_left_X = float('-inf')
            else:
                max_left_X = nums1[cut_x - 1]
            if cut_x == len_nums1:
                min_right_X = float('inf')
            else:
                min_right_X = nums1[cut_x]

            if cut_y == 0:
                max_left_Y = float('-inf')
            else:
                max_left_Y = nums2[cut_y - 1]
            if cut_y == len_nums2:
                min_right_Y = float('inf')
            else:
                min_right_Y = nums2[cut_y]

            if max_left_X <= min_right_Y and max_left_Y <= min_right_X:
                if total_length % 2 == 0:
                    return (max(max_left_X, max_left_Y) + min(min_right_X, min_right_Y)) / 2.0
                else:
                    return max(max_left_X, max_left_Y)
            elif max_left_X > min_right_Y:
                cut_x -= 1
            else:
                cut_x += 1
