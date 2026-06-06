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

        # create rows list to store str for each row
        rows = [""]*numRows
        current_row = 0
        step = 1

        for char in s:
            rows[current_row] += char

            # if it reaches the last char in the str
            if current_row == numRows-1:
                # step becomes going backward
                step = -1
            # if it returns to the begining
            elif current_row == 0:
                # step becomes moving forward again
                step = 1

            current_row += step

        # finally combine all rows to one str
        return ''.join(rows)


def test_solution():
    solution = Solution()

    test_cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
        ("ABCDEF", 2, "ACEBDF"),
    ]

    for i, (s, numRows, expected) in enumerate(test_cases, 1):
        result = solution.convert(s, numRows)
        print(f"Test Case {i}:")
        print(f"Input: s = '{s}', numRows = {numRows}")
        print(f"Expected Output: '{expected}'")
        print(f"Actual Output: '{result}'")
        print("Status: ", "PASS" if result == expected else "FAIL")
        print()


if __name__ == "__main__":
    test_solution()
