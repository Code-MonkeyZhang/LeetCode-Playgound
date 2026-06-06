from typing import List

"""
题目简述：
给定一个有序数组 nums，要求原地删除多余的重复项，
使得每个元素最多出现两次，并返回删除后数组的新长度。

示例：
输入: [1,1,1,2,2,3]
输出: 长度 = 5, 数组前5个元素为 [1,1,2,2,3]

输入: [0,0,1,1,1,1,2,3,3]
输出: 长度 = 7, 数组前7个元素为 [0,0,1,1,2,3,3]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # TODO: 在这里写你的解法
        life = 1
        index = 0
        buffer = None

        for i in range(len(nums)):
            if nums[i] != buffer:
                # 如果不等于buffer,就加入stack
                nums[index] = nums[i]
                index += 1
                buffer = nums[i]
                life = 1
            else:
                # 如果等于buffer life > 0, 照样加入stack,但是life--
                if life > 0: 
                    nums[index] = nums[i]
                    index += 1
                    life -= 1
            
        return index
            



# ------------------- 测试环境 -------------------
def run_tests():
    sol = Solution()

    tests = [
        {
            "input": [1,1,1,2,2,3],
            "expected_len": 5,
            "expected_nums": [1,1,2,2,3]
        },
        {
            "input": [0,0,1,1,1,1,2,3,3],
            "expected_len": 7,
            "expected_nums": [0,0,1,1,2,3,3]
        },
        {
            "input": [1,1,2,2,3,3],
            "expected_len": 6,
            "expected_nums": [1,1,2,2,3,3]
        },
        {
            "input": [1],
            "expected_len": 1,
            "expected_nums": [1]
        },
        {
            "input": [1,1,1,1],
            "expected_len": 2,
            "expected_nums": [1,1]
        }
    ]

    for i, test in enumerate(tests, 1):
        nums = test["input"][:]  # 拷贝一份，避免修改原始数据
        length = sol.removeDuplicates(nums)

        print(f"\nTest Case {i}:")
        print(f"输入: {test['input']}")
        print(f"期待长度: {test['expected_len']}, 实际长度: {length}")
        print(f"期待数组: {test['expected_nums']}, 实际数组: {nums[:length]}")
        print("结果:", "✅ 正确" if (length == test['expected_len'] and nums[:length] == test['expected_nums']) else "❌ 错误")


if __name__ == "__main__":
    run_tests()
