# LeetCode 367 — 有效的完全平方数
#
# 题目描述：给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 true，否则返回 false。
# 不要使用任何内置的库函数，如 sqrt。
#
# 示例 1：输入: num = 16 → 输出: true
# 示例 2：输入: num = 14 → 输出: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # TODO: 在这里实现你的逻辑
        left = 0
        right = num

        while left <= right: 
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid - 1
            elif mid ** 2 > num:
                right = mid + 1
        
        return False


def run_tests():
    solution = Solution()
    test_cases = [
        # (输入, 期待输出)
        (16, True),   # 题目示例，4*4=16
        (14, False),  # 题目示例，不是完全平方数
        (1, True),    # 边界情况，1=1*1
        (2, False),   # 最小非平方数
        (4, True),    # 2*2
        (9, True),    # 3*3
        (15, False),  # 介于 3*3 和 4*4 之间
        (25, True),   # 5*5
        (26, False),  # 紧邻完全平方数
        (2147395600, True),  # 46340^2，接近 2^31 边界
        (2147483647, False), # 题目范围上限，不是平方数
    ]
    
    for i, (num, expected) in enumerate(test_cases, 1):
        output = solution.isPerfectSquare(num)
        print(f"Test case {i}: num={num}")
        print(f"  Expected: {expected}")
        print(f"  Output:   {output}")
        print(f"  Result:   {'PASS' if output == expected else 'FAIL'}\n")


if __name__ == "__main__":
    run_tests()
