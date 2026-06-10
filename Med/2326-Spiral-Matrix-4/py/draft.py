# LeetCode 2326 — 螺旋矩阵 IV
#
# 题目描述：给你两个整数 m 和 n，以及一个头节点为 head 的链表。请你生成一个 m x n 的螺旋矩阵，
# 矩阵包含链表中的所有节点，按照顺时针螺旋顺序填充。如果链表节点不足，剩余位置用 -1 填充。
#
# 示例 1：输入: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
#         → 输出: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# 示例 2：输入: m = 1, n = 4, head = [0,1,2] → 输出: [[0,1,2,-1]]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from typing import List
from ds_utils.single_linked_list import ListNode


class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
