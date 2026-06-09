# LeetCode 21 — 合并两个有序链表
#
# 题目描述：将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例 1：输入: l1 = [1,2,4], l2 = [1,3,4] → 输出: [1,1,2,3,4,4]
# 示例 2：输入: l1 = [], l2 = [] → 输出: []
# 示例 3：输入: l1 = [], l2 = [0] → 输出: [0]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Optional
from ds_utils.single_linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(val=0, next=None)
        cur = dummy
        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            cur = cur.next

        cur.next = ptr1 or ptr2
        return dummy.next
