# LeetCode 21 — 合并两个有序链表
#
# 题目描述：将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例 1：输入: l1 = [1,2,4], l2 = [1,3,4] → 输出: [1,1,2,3,4,4]
# 示例 2：输入: l1 = [], l2 = [] → 输出: []
# 示例 3：输入: l1 = [], l2 = [0] → 输出: [0]

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from typing import Optional
from ds_utils.single_linked_list import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
