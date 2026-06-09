# LeetCode 141 — 环形链表
#
# 题目描述：给你一个链表的头节点 head，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
#
# 示例 1：输入: head = [3,2,0,-4], pos = 1 → 输出: true（尾节点连接到第1个节点）
# 示例 2：输入: head = [1,2], pos = 0 → 输出: true（尾节点连接到第0个节点）
# 示例 3：输入: head = [1], pos = -1 → 输出: false（无环）

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Optional
from ds_utils.single_linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while (
            slow.next is not None
            and fast.next is not None
            and fast.next.next is not None
        ):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
