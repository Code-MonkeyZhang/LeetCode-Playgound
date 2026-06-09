# LeetCode 3 — 无重复字符的最长子串
#
# 题目描述：给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例 1：输入: s = "abcabcbb" → 输出: 3（无重复字符的最长子串是 "abc"，长度为3）
# 示例 2：输入: s = "bbbbb" → 输出: 1（无重复字符的最长子串是 "b"，长度为1）
# 示例 3：输入: s = "pwwkew" → 输出: 3（无重复字符的最长子串是 "wke"，长度为3）


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_seen = {}
        start = 0
        longest_step = 0
        current_step = 0

        for i, char in enumerate(s):
            if char in char_seen and char_seen[char] >= start:
                start = char_seen[char] + 1
                current_step = i - start + 1
            else:
                current_step += 1
                longest_step = max(longest_step, current_step)

            char_seen[char] = i

        return longest_step
