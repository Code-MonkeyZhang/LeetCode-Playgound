#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeetCode 141. Linked List Cycle — Test Harness (Python)

Problem (brief):
Given the head of a singly linked list, determine if the list has a cycle.
A cycle exists if a node can be reached again by continuously following the next pointer.

Simple examples:
- head = [3,2,0,-4], pos = 1  -> True   (tail connects to index 1, value 2)
- head = [1,2], pos = 0       -> True   (tail connects back to head)
- head = [1], pos = -1        -> False  (no cycle)

How to use:
1) Implement Solution.hasCycle(self, head) below (keep the function signature).
2) Run this file. It will build multiple independent test cases (not packed into a single array),
   then print Expected vs Actual for each, plus pass/fail stats at the end.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Optional, Tuple, Callable, List
from ds_utils.single_linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Implement your solution here.
        """
        """
        思路: 快慢指针
        slow = head
        fast = head
        slow一次走一步,fast一次走两步,如果这个链表是环,那么slow就会与fast相遇

        edge cases: 链表为空,或者只有一个node,不能跑next.next
        """

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


# ---------------------- Helpers to build / label test cases ----------------------


def build_list_with_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    """
    Build a singly linked list from values.
    If pos >= 0, connect the tail's next to the node at index=pos to form a cycle.
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        if pos < 0 or pos >= len(nodes):
            raise ValueError("pos must be -1 or a valid index within the list")
        nodes[-1].next = nodes[pos]
    return nodes[0]


def format_bool(b: Optional[bool]) -> str:
    return "True" if b is True else ("False" if b is False else str(b))


# Each case builder returns: (head, expected, name)
def case_example_1() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [3, 2, 0, -4], 1, True
    return (
        build_list_with_cycle(vals, pos),
        expected,
        "Example 1: [3,2,0,-4], pos=1 → True",
    )


def case_example_2() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [1, 2], 0, True
    return build_list_with_cycle(vals, pos), expected, "Example 2: [1,2], pos=0 → True"


def case_example_3() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [1], -1, False
    return build_list_with_cycle(vals, pos), expected, "Example 3: [1], pos=-1 → False"


def case_empty_list() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [], -1, False
    return build_list_with_cycle(vals, pos), expected, "Edge: empty list → False"


def case_single_cycle() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [7], 0, True
    return (
        build_list_with_cycle(vals, pos),
        expected,
        "Edge: single node cycle [7], pos=0 → True",
    )


def case_no_cycle_longer() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [1, 2, 3, 4, 5], -1, False
    return (
        build_list_with_cycle(vals, pos),
        expected,
        "No cycle: [1,2,3,4,5], pos=-1 → False",
    )


def case_cycle_middle() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = (
        [10, 20, 30, 40, 50],
        2,
        True,
    )  # tail connects to node with value 30
    return (
        build_list_with_cycle(vals, pos),
        expected,
        "Cycle: [10,20,30,40,50], pos=2 → True",
    )


def case_two_nodes_no_cycle() -> Tuple[Optional[ListNode], bool, str]:
    vals, pos, expected = [4, 5], -1, False
    return (
        build_list_with_cycle(vals, pos),
        expected,
        "Two nodes, no cycle: [4,5], pos=-1 → False",
    )


# ------------------------------- Test Runner -------------------------------------


def run_case(build_fn: Callable[[], Tuple[Optional[ListNode], bool, str]]) -> bool:
    name = "<unnamed>"
    try:
        head, expected, name = build_fn()
        sol = Solution()
        actual = sol.hasCycle(head)
        ok = actual == expected
        status = "✅ CORRECT" if ok else "❌ WRONG"
        print(f"[{status}] {name}")
        print(f"    Expected: {format_bool(expected)}")
        print(f"    Actual:   {format_bool(actual)}\n")
        return ok
    except NotImplementedError as nie:
        print(f"[⏭️ SKIPPED] {name} — Solution not implemented: {nie}\n")
        return False
    except Exception as e:
        print(f"[💥 ERROR] {name} — Exception during run: {e}\n")
        return False


def main():
    print("=" * 78)
    print("LeetCode 141 • Linked List Cycle — Testing Environment")
    print("=" * 78 + "\n")

    # Register cases individually (kept separate for easy breakpointing)
    # You can comment/uncomment specific cases as needed.
    test_cases = [
        case_example_1,
        case_example_2,
        case_example_3,
        case_empty_list,
        case_single_cycle,
        case_no_cycle_longer,
        case_cycle_middle,
        case_two_nodes_no_cycle,
    ]

    passed = 0
    total = 0
    for build_fn in test_cases:
        total += 1
        if run_case(build_fn):
            passed += 1

    print("-" * 78)
    print(f"Passed {passed} / {total} tests.")
    if passed == total:
        print("🎉 Awesome! All tests passed — you nailed it!")
    else:
        print("Keep going! Tweak your implementation and re-run the tests. 💪")


if __name__ == "__main__":
    main()
