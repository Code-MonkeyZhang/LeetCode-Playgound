# LeetCode 13 — 罗马数字转整数
#
# 题目描述：给定一个罗马数字，将其转换成整数。
#
# 示例 1：输入: s = "III" → 输出: 3
# 示例 2：输入: s = "LVIII" → 输出: 58
# 示例 3：输入: s = "MCMXCIV" → 输出: 1994

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result
