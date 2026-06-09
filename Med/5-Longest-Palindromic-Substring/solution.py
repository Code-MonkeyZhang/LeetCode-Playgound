# LeetCode 5 — 最长回文子串
#
# 题目描述：给你一个字符串 s，找到 s 中最长的回文子串。
#
# 示例 1：输入: s = "babad" → 输出: "bab"（或 "aba"）
# 示例 2：输入: s = "cbbd" → 输出: "bb"


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        max_length = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    result = s[left:right+1]
                    max_length = right - left + 1
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    result = s[left:right+1]
                    max_length = right - left + 1
                left -= 1
                right += 1

        return result
