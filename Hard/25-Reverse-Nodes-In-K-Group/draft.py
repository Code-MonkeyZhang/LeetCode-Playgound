# LeetCode 25 — K个一组翻转链表
#
# 题目描述：给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，
# 那么请将最后剩余的节点保持原有顺序。不能只是单纯改变节点内部的值，而是需要实际进行节点交换。
#
# 示例 1：输入: head = [1,2,3,4,5], k = 2 → 输出: [2,1,4,3,5]
# 示例 2：输入: head = [1,2,3,4,5], k = 3 → 输出: [3,2,1,4,5]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ds_utils.single_linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass
