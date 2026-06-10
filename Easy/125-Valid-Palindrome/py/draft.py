# LeetCode 125 — 验证回文串
#
# 题目描述：给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1：输入: s = "A man, a plan, a canal: Panama" → 输出: true
# 示例 2：输入: s = "race a car" → 输出: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
