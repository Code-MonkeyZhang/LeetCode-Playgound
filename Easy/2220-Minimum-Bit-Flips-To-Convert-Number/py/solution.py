# LeetCode 2220 — 转换数字的最少位翻转次数
#
# 题目描述：给定两个整数 start 和 goal，返回将 start 转换为 goal 所需的最少位翻转次数。
# 位翻转是指将二进制表示中的某一位从 0 变为 1，或从 1 变为 0。
#
# 示例 1：输入: start = 10, goal = 7 → 输出: 3（1010 → 0111，翻转3位）
# 示例 2：输入: start = 3, goal = 4 → 输出: 3（011 → 100，翻转3位）

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        result = 0
        for char in bin(xor):
            if char == "1":
                result += 1
        return result

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
