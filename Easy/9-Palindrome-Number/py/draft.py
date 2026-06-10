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
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
