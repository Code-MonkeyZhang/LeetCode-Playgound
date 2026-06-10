# LeetCode 12 — 整数转罗马数字
#
# 题目描述：给你一个整数 num，将其转为罗马数字。
#
# 示例 1：输入: num = 3749 → 输出: "MMMDCCXLIX"
# 示例 2：输入: num = 58 → 输出: "LVIII"
# 示例 3：输入: num = 1994 → 输出: "MCMXCIV"

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        store_int_roman = [
            [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
            [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
            [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]
        ]
        for i in range(len(store_int_roman)):
            while num >= store_int_roman[i][0]:
                roman += store_int_roman[i][1]
                num -= store_int_roman[i][0]
        return roman

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
