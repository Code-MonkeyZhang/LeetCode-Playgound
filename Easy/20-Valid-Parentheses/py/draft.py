# LeetCode 20 — 有效的括号
#
# 题目描述：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。
# 有效字符串需满足：左括号必须用相同类型的右括号闭合，左括号必须以正确的顺序闭合。
#
# 示例 1：输入: s = "()" → 输出: true
# 示例 2：输入: s = "()[]{}" → 输出: true
# 示例 3：输入: s = "(]" → 输出: false

class Solution:
    def isValid(self, s: str) -> bool:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
