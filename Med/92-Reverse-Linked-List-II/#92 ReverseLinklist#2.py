# LeetCode 92 — 反转链表 II
#
# 题目描述：给你单链表的头指针 head 和两个整数 left 和 right，其中 left <= right。
# 请你反转从位置 left 到位置 right 的链表节点，返回反转后的链表。
#
# 示例 1：输入: head = [1,2,3,4,5], left = 2, right = 4 → 输出: [1,4,3,2,5]
# 示例 2：输入: head = [5], left = 1, right = 1 → 输出: [5]

# Definition for singly-linked list.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ds_utils.single_linked_list import ListNode


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    def reverseBetween(self, head, left, right):
        # 在这里粘贴您的reverseBetween函数的实现
        if head.next is None and left == right:
            return head

        dummy = ListNode(0, head)
        start = dummy
        for _ in range(left-1):
            start = start.next

        curr = start.next
        next = curr.next

        for _ in range(right-left):
            temp = next.next
            next.next = curr
            curr = next
            next = temp

        temp = start.next
        start.next = curr
        temp.next = next

        return dummy.next

    # def reverseBetween(self, head, left, right):
        dummy = ListNode(val=0,next=head)
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        
        cur = prev.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
        
        return dummy.next


# 测试用例
def test_reverse_between():
    solution = Solution()

    # 测试用例 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseBetween(head1, 2, 4)
    assert linked_list_to_list(result1) == [
        1, 4, 3, 2, 5], "Test case 1 failed"

    # 测试用例 2
    head2 = create_linked_list([5])
    result2 = solution.reverseBetween(head2, 1, 1)
    assert linked_list_to_list(result2) == [5], "Test case 2 failed"

    # 测试用例 3: 反转整个链表
    head3 = create_linked_list([1, 2, 3, 4, 5])
    result3 = solution.reverseBetween(head3, 1, 5)
    assert linked_list_to_list(result3) == [
        5, 4, 3, 2, 1], "Test case 3 failed"

    # 测试用例 4: 反转中间部分
    head4 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    result4 = solution.reverseBetween(head4, 3, 5)
    assert linked_list_to_list(result4) == [
        1, 2, 5, 4, 3, 6, 7], "Test case 4 failed"

    print("All test cases passed!")


# 运行测试
if __name__ == "__main__":
    test_reverse_between()
