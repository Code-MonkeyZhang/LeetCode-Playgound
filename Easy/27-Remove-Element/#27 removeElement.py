"""
题目描述：
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。
元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

你需要保证：
- 修改 nums，使前 k 个元素是不等于 val 的。
- 返回的 k 是不等于 val 的元素数量。
- k 之后的元素内容无关紧要。

示例：
输入: nums = [3,2,2,3], val = 3
输出: 2, nums = [2,2,_,_]

输入: nums = [0,1,2,2,3,0,4,2], val = 2
输出: 5, nums = [0,1,4,0,3,_,_,_]
"""

"""
[0,1,3,0,4,2]
"""


# 待实现函数
def removeElement(nums, val):
    # TODO: 在这里实现你的逻辑
    
    # 暴力解法
    # n = len(nums) # 需要一个变量来存储长度,后面还可以用来限制循环的数量
    # for i in range(n):
    #     if nums[i] == val:
    #         # 如果遇到要删除的元素, 把后面的元素都向前移一位
    #         for j in range(i + 1,n):
    #             nums[j-1] = nums[j]
    #         n -= 1
    # return n

    # 聪明解法
    index = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    
    return index


# -------------------- 测试环境 --------------------
def run_test(nums, val, expected_nums):
    print(f"\n输入: nums={nums}, val={val}")
    k = removeElement(nums, val)
    
    print("返回的 k:", k)
    print("期望的 k:", len(expected_nums))

    # 对前k个元素排序以便比较
    result = sorted(nums[:k])
    expected_sorted = sorted(expected_nums)

    print("输出的前 k 个元素:", result)
    print("期望的前 k 个元素:", expected_sorted)
    print("测试结果:", "✅ 通过" if result == expected_sorted and k == len(expected_nums) else "❌ 不通过")


if __name__ == "__main__":
    # 测试用例
    run_test([3,2,2,3], 3, [2,2])
    run_test([0,1,2,2,3,0,4,2], 2, [0,1,3,0,4])
    run_test([], 0, [])
    run_test([1,1,1,1], 1, [])
    run_test([4,5], 4, [5])
    run_test([2,2,3], 2, [3])
