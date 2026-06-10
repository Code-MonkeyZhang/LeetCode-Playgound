# LeetCode 7 — 整数反转
#
# 题目描述：给你一个 32 位的有符号整数 x，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位有符号整数的范围 [-2^31, 2^31-1]，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
# 示例 1：输入: x = 123 → 输出: 321
# 示例 2：输入: x = -123 → 输出: -321
# 示例 3：输入: x = 120 → 输出: 21


class Solution:
    def reverse(self, x: int) -> int:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
