# LeetCode 6 — Z字形变换
#
# 题目描述：将一个给定字符串 s 根据给定的行数 numRows，以从上往下、从左到右进行 Z 字形排列。
# 然后从左到右逐行读取，产生一个新的字符串。
#
# 示例 1：输入: s = "PAYPALISHIRING", numRows = 3 → 输出: "PAHNAPLSIIGYIR"
# 示例 2：输入: s = "PAYPALISHIRING", numRows = 4 → 输出: "PINALSIGYAHRPI"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        if numRows == 1:
            return s

        rows = [""] * numRows
        current_row = 0
        step = 1

        for char in s:
            rows[current_row] += char

            if current_row == numRows - 1:
                step = -1
            elif current_row == 0:
                step = 1

            current_row += step

        return ''.join(rows)
