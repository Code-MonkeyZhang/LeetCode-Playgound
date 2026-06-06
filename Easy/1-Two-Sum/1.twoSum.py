# LeetCode 1 — 两数之和
#
# 题目描述：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target
# 的那两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案，且不能使用同一个元素两次。
#
# 示例 1：输入: nums = [2,7,11,15], target = 9 → 输出: [0,1]
# 示例 2：输入: nums = [3,2,4], target = 6 → 输出: [1,2]
# 示例 3：输入: nums = [3,3], target = 6 → 输出: [0,1]

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
Ideas/thoughts:
第一次遍历建一个hashtable,把所有东西存起来 O(n)
第二次遍历每个数,就可以检查target-num[i] 是否在hashtable里面,判断的时候要排除它自己 O(n)

complexity: O(n)
"""


def twoSum(nums, target):
    # create hashtable
    numMap = {}
    size = len(nums)

    # 1st iteration, put nums in hashtable
    for i in range(size):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(size):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []


def test_twoSum():
    test1 = [2, 7, 11, 15]
    target1 = 9
    test2 = [3, 2, 4]
    target2 = 6
    test3 = [3, 3]
    target3 = 6

    print(twoSum(test1, target1))
    print(twoSum(test2, target2))
    print(twoSum(test3, target3))


if __name__ == '__main__':
    test_twoSum()
