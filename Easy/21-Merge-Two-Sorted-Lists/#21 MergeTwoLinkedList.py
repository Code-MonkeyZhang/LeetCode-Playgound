# LeetCode 21 — 合并两个有序链表
#
# 题目描述：将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例 1：输入: l1 = [1,2,4], l2 = [1,3,4] → 输出: [1,1,2,3,4,4]
# 示例 2：输入: l1 = [], l2 = [] → 输出: []
# 示例 3：输入: l1 = [], l2 = [0] → 输出: [0]

"""
LeetCode 21: Merge Two Sorted Lists

Problem (brief):
Given two singly linked lists l1 and l2 where the nodes are sorted in non-decreasing order,
merge them into a single sorted linked list and return its head.

Simple Examples:
1) l1 = [1,2,4], l2 = [1,3,4]  ->  [1,1,2,3,4,4]
2) l1 = [],       l2 = []       ->  []
3) l1 = [],       l2 = [0]      ->  [0]
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Optional, Iterable, List, Tuple, Any
from ds_utils.single_linked_list import ListNode


# === Utilities: build & inspect linked lists ===


def build_linked_list(values: Iterable[int]) -> Optional[ListNode]:
    head = tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


def lists_equal(a: Optional[ListNode], b: Optional[ListNode]) -> bool:
    pa, pb = a, b
    while pa and pb:
        if pa.val != pb.val:
            return False
        pa, pb = pa.next, pb.next
    return pa is None and pb is None


# === Your solution goes here ===
# Paste your Solution class below. Keep the class name and method signature.
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # TODO: Implement your solution.

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


# === Test runner ===

_total = 0
_passed = 0


def _print_case_header(
    title: str, l1_in: List[int], l2_in: List[int], expected: List[int]
) -> None:
    print("=" * 64)
    print(title)
    print("-" * 64)
    print(f"Input l1: {l1_in}")
    print(f"Input l2: {l2_in}")
    print(f"Expected: {expected}")


def _print_case_result(actual: Any, ok: bool) -> None:
    print(f"Actual:   {actual}")
    print(f"Correct:  {ok}")


def run_test_case(
    title: str, l1_in: List[int], l2_in: List[int], expected: List[int]
) -> None:
    global _total, _passed
    _total += 1

    _print_case_header(title, l1_in, l2_in, expected)

    l1 = build_linked_list(l1_in)
    l2 = build_linked_list(l2_in)
    expected_ll = build_linked_list(expected)

    try:
        result = Solution().mergeTwoLists(l1, l2)
        actual_list = linked_list_to_list(result)
        ok = lists_equal(result, expected_ll)
        _print_case_result(actual_list, ok)
        if ok:
            _passed += 1
    except Exception as e:
        _print_case_result(f"<raised {type(e).__name__}: {e}>", False)


def print_summary() -> None:
    print("=" * 64)
    print(f"Passed: {_passed}/{_total} tests")
    if _passed == _total and _total > 0:
        print("All green! 🎉 Great job — on to the next one!")
    elif _passed == 0:
        print("No worries — step through a case, set a breakpoint, and try again.")
    else:
        print("Getting there! Review the failing cases and iterate.")


if __name__ == "__main__":
    # --- Separate test cases (not packed into a single array) ---
    # Feel free to set breakpoints on individual calls to run_test_case.

    # Case 1: Example
    run_test_case(
        title="Case 1: Typical merge",
        l1_in=[1, 2, 4],
        l2_in=[1, 3, 4],
        expected=[1, 1, 2, 3, 4, 4],
    )

    # Case 2: Both empty
    run_test_case(
        title="Case 2: Both lists empty",
        l1_in=[],
        l2_in=[],
        expected=[],
    )

    # Case 3: One empty
    run_test_case(
        title="Case 3: First empty, second non-empty",
        l1_in=[],
        l2_in=[0],
        expected=[0],
    )

    # Case 4: Already interleaved
    run_test_case(
        title="Case 4: Interleaved values",
        l1_in=[1, 3, 5],
        l2_in=[2, 4, 6],
        expected=[1, 2, 3, 4, 5, 6],
    )

    # Case 5: Duplicates across lists
    run_test_case(
        title="Case 5: Duplicates present",
        l1_in=[1, 1, 2],
        l2_in=[1, 1, 3],
        expected=[1, 1, 1, 1, 2, 3],
    )

    # Case 6: Negative values and range coverage
    run_test_case(
        title="Case 6: Negatives and positives",
        l1_in=[-100, -2, 0, 2],
        l2_in=[-100, -50, -3, 3],
        expected=[-100, -100, -50, -3, -2, 0, 2, 3],
    )

    # Print final summary
    print_summary()
