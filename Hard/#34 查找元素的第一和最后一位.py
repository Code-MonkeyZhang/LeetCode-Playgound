from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        TODO: 在这里实现题目的逻辑
        要求: 时间复杂度 O(log n)
        """

        """ 
        思路:
        一次二分找“第一个等于 target 的位置”（命中继续往左收缩），
        一次二分找“最后一个等于 target 的位置”（命中继续往右推进）；
        命中位置用 idx 记录，循环结束返回。
        """

        def binarySearch(isLeft: bool) -> int:
            left = 0
            right = len(nums) - 1
            index = -1 

            while left <= right: 
                mid = (left + right) // 2
                if nums[mid] == target: 
                    index = mid
                    # 如果是查找左元素, 要不断缩有阿宾的
                    if isLeft: 
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            
            return index
        
        left = binarySearch(True)
        right = binarySearch(False)

        return [left, right]
        





# ----------------- 测试环境 -----------------
def run_tests():
    sol = Solution()
    test_cases = [
        # (输入数组, 目标值, 期望输出)
        ([5,7,7,8,8,10], 8, [3,4]),
        ([5,7,7,8,8,10], 6, [-1,-1]),
        ([], 0, [-1,-1]),
        ([1], 1, [0,0]),
        ([1], 2, [-1,-1]),
        ([2,2,2,2,2], 2, [0,4]),  # 全是相同元素
        ([1,2,3,4,5,6,7], 4, [3,3]),  # 单个元素出现一次
        ([1,2,3,4,4,4,5,6], 4, [3,5]),  # 多个连续元素
        ([1,3,5,7,9], 10, [-1,-1]),  # 大于所有元素
        ([1,3,5,7,9], -5, [-1,-1]),  # 小于所有元素
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.searchRange(nums, target)
        print(f"Test Case {i}: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Passed" if result == expected else "❌ Failed")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
