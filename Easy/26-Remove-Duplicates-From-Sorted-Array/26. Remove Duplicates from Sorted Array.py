# LeetCode 26 — 删除有序数组中的重复项
#
# 题目描述：给你一个非严格递增排列的数组 nums，请你原地删除重复出现的元素，使每个元素只出现一次，
# 返回删除后数组的新长度。元素的相对顺序应该保持一致。然后返回 nums 中唯一元素的个数。
#
# 示例 1：输入: nums = [1,1,2] → 输出: 2, nums = [1,2,_]
# 示例 2：输入: nums = [0,0,1,1,1,2,2,3,3,4] → 输出: 5, nums = [0,1,2,3,4,_,_,_,_,_]

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, k = 1, 1
        m = nums[0]
        while n < len(nums):
            if nums[n] == m:
                n += 1
            else:
                nums[k] = nums[n]
                m = nums[n]
                k += 1
        return k


def test_remove_duplicates():
    solution = Solution()

    # 测试用例 1
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(f"测试用例 1: k = {k1}, nums = {nums1[:k1]}")
    assert k1 == 2 and nums1[:k1] == [1, 2], "测试用例 1 失败"

    # 测试用例 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(f"测试用例 2: k = {k2}, nums = {nums2[:k2]}")
    assert k2 == 5 and nums2[:k2] == [0, 1, 2, 3, 4], "测试用例 2 失败"

    # 测试用例 3 (没有重复元素)
    nums3 = [1, 2, 3, 4, 5]
    k3 = solution.removeDuplicates(nums3)
    print(f"测试用例 3: k = {k3}, nums = {nums3[:k3]}")
    assert k3 == 5 and nums3[:k3] == [1, 2, 3, 4, 5], "测试用例 3 失败"

    # 测试用例 4 (全是重复元素)
    nums4 = [1, 1, 1, 1, 1]
    k4 = solution.removeDuplicates(nums4)
    print(f"测试用例 4: k = {k4}, nums = {nums4[:k4]}")
    assert k4 == 1 and nums4[:k4] == [1], "测试用例 4 失败"

    # 测试用例 5 (包含负数)
    nums5 = [-3, -1, -1, 0, 0, 0, 0, 0, 2]
    k5 = solution.removeDuplicates(nums5)
    print(f"测试用例 5: k = {k5}, nums = {nums5[:k5]}")
    assert k5 == 4 and nums5[:k5] == [-3, -1, 0, 2], "测试用例 5 失败"

    print("所有测试用例通过！")


# 运行测试
test_remove_duplicates()
