# LeetCode 725 — 分隔链表
#
# 题目描述：给你一个头结点为 head 的单链表和一个整数 k，请你设计一个算法将链表分隔为 k 个连续的部分。
# 每部分的长度应该尽可能相等：任意两部分的长度差距不超过1。排在前面的部分长度应该大于或等于排在后面的长度。
#
# 示例 1：输入: head = [1,2,3], k = 5 → 输出: [[1],[2],[3],[],[]]
# 示例 2：输入: head = [1,2,3,4,5,6,7,8,9,10], k = 3 → 输出: [[1,2,3,4],[5,6,7],[8,9,10]]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from typing import List
from ds_utils.single_linked_list import ListNode


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        if head is None:
            return [None] * k

        iter = head
        length = 0
        while iter is not None:
            iter = iter.next
            length += 1

        size = length // k
        remain = length % k

        group_size = [size] * k
        for i in range(remain):
            group_size[i] += 1

        result = []
        iter = head
        for size in group_size:
            if size == 0:
                result.append(None)
                continue
            dummy = iter
            for _ in range(size):
                temp = iter
                iter = iter.next
            temp.next = None
            result.append(dummy)

        return result

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
