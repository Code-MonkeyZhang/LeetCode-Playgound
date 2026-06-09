# LeetCode 9 — 回文数
#
# 题目描述：给你一个整数 x，如果 x 是一个回文整数，返回 true；否则，返回 false。
# 回文数是指正序和倒序读都一样的整数。
#
# 示例 1：输入: x = 121 → 输出: true
# 示例 2：输入: x = -121 → 输出: false
# 示例 3：输入: x = 10 → 输出: false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        temp = x
        reverse_num = 0
        while temp > reverse_num:
            digit = temp % 10
            reverse_num = 10 * reverse_num + digit
            temp = temp // 10
        return reverse_num == temp or reverse_num // 10 == temp
