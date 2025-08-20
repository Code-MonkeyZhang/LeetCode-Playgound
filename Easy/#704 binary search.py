from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            
        return -1





if __name__ == "__main__":
    s = Solution()
    
    # 题目示例
    print(s.search([-1,0,3,5,9,12], 9))   # 预期 4
    print(s.search([-1,0,3,5,9,12], 2))   # 预期 -1

    # 边界情况
    print(s.search([1], 1))               # 预期 0（只有一个数，刚好命中）
    print(s.search([1], 0))               # 预期 -1（只有一个数，但没找到）

    # 数组只有两个数
    print(s.search([1,2], 1))             # 预期 0
    print(s.search([1,2], 2))             # 预期 1
    print(s.search([1,2], 3))             # 预期 -1

    # 大一点的数组
    print(s.search([1,3,5,7,9,11,13,15], 7))   # 预期 3
    print(s.search([1,3,5,7,9,11,13,15], 14))  # 预期 -1
