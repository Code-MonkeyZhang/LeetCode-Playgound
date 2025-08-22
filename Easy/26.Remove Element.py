"""
LeetCode 26: 删除有序数组中的重复项

题目描述:
给你一个非严格递增排列的数组 nums，请你原地删除重复出现的元素，
使每个元素只出现一次，并返回删除后数组的新长度。
元素的相对顺序应保持一致。

示例:
输入: nums = [1,1,2]
输出: 2, nums = [1,2,_]

输入: nums = [0,0,1,1,1,2,2,3,3,4]
输出: 5, nums = [0,1,2,3,4,_]
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # TODO: 在这里实现你的方法
        index = 0
        buffer = None
        for i in range(len(nums)):
            # 如果和buffer不相等
            # 就添加这个数到stack, 同时更新buffer
            if nums[i] != buffer:
                nums[index] = nums[i]
                index += 1
                buffer = nums[i]

        return index


def run_tests():
    solution = Solution()
    
    test_cases = [
        # (输入, 期望返回长度, 期望修改后的数组)
        ([1,1,2], 2, [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
        ([1,2,3,4,5], 5, [1,2,3,4,5]),       # 没有重复
        ([1,1,1,1,1], 1, [1]),               # 全部相同
        ([1,1,2,2,3,3,4,4,5,5], 5, [1,2,3,4,5]), # 两两重复
        ([0], 1, [0]),                       # 单元素
    ]
    
    for i, (nums, expected_len, expected_nums) in enumerate(test_cases, 1):
        nums_copy = nums[:]  # 复制避免修改原始数据
        k = solution.removeDuplicates(nums_copy)
        # 校验前 k 个元素是否符合预期
        is_correct = (k == expected_len and nums_copy[:k] == expected_nums)
        
        print(f"Test Case {i}:")
        print(f"输入: {nums}")
        print(f"期望长度: {expected_len}, 实际长度: {k}")
        print(f"期望数组前k: {expected_nums}, 实际数组前k: {nums_copy[:k]}")
        print(f"结果: {'✅ 正确' if is_correct else '❌ 错误'}\n")


if __name__ == "__main__":
    run_tests()
