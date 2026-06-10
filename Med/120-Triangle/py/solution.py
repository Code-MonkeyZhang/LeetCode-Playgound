# LeetCode 120 — 三角形最小路径和
#
# 题目描述：给定一个三角形 triangle，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的节点上。相邻节点指的是下标与当前节点下标相同或等于当前节点下标+1 的两个节点。
#
# 示例 1：输入: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]] → 输出: 11（路径 2→3→5→1 的和为11）
# 示例 2：输入: triangle = [[-10]] → 输出: -10

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        layer = len(triangle)
        for i in range(layer - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
