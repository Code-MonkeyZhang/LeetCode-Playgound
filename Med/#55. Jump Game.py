from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num >= dest-i:
                dest = i

        return dest == 0


solution = Solution()

# 测试用例 1
print(solution.canJump([2, 3, 1, 1, 4]))  # 应该返回 True

# 测试用例 2
print(solution.canJump([3, 2, 1, 0, 4]))  # 应该返回 False
