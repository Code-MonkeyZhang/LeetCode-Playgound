# LeetCode 367 — 有效的完全平方数
#
# 题目描述：给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 true，否则返回 false。
# 不要使用任何内置的库函数，如 sqrt。
#
# 示例 1：输入: num = 16 → 输出: true
# 示例 2：输入: num = 14 → 输出: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
