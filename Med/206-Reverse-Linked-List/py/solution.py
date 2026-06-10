# LeetCode 206 — 反转链表
#
# 题目描述：给你单链表的头节点 head，请你反转链表，并返回反转后的链表。
#
# 示例 1：输入: head = [1,2,3,4,5] → 输出: [5,4,3,2,1]
# 示例 2：输入: head = [1,2] → 输出: [2,1]
# 示例 3：输入: head = [] → 输出: []

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ds_utils.single_linked_list import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
