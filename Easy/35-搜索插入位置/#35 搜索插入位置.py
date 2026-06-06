# LeetCode 35 — 搜索插入位置
#
# 题目描述：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。时间复杂度为 O(log n)。
#
# 示例 1：输入: nums = [1,3,5,6], target = 5 → 输出: 2
# 示例 2：输入: nums = [1,3,5,6], target = 2 → 输出: 1
# 示例 3：输入: nums = [1,3,5,6], target = 7 → 输出: 4

def searchInsert(nums, target):
    """
    TODO: 在这里实现题目的逻辑
    要求: 时间复杂度 O(log n)
    """
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
        
    return left


# ----------------- 测试环境 -----------------
def run_tests():
    test_cases = [
        # (输入数组, 目标值, 期望输出)
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
        ([1], 2, 1),
        ([1, 3], 3, 1),
        ([1, 3], 2, 1),
        ([1, 3, 5, 6, 8, 10], 9, 5),  # 额外 case
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = searchInsert(nums, target)
        print(f"Test Case {i}: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Passed" if result == expected else "❌ Failed")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
