# LeetCode 725 — 分隔链表
#
# 题目描述：给你一个头结点为 head 的单链表和一个整数 k，请你设计一个算法将链表分隔为 k 个连续的部分。
# 每部分的长度应该尽可能相等：任意两部分的长度差距不超过1。排在前面的部分长度应该大于或等于排在后面的长度。
#
# 示例 1：输入: head = [1,2,3], k = 5 → 输出: [[1],[2],[3],[],[]]
# 示例 2：输入: head = [1,2,3,4,5,6,7,8,9,10], k = 3 → 输出: [[1,2,3,4],[5,6,7],[8,9,10]]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import List
from ds_utils.single_linked_list import ListNode


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        pass
