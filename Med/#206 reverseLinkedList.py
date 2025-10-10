"""
LeetCode 206. Reverse Linked List
---------------------------------
Given the head of a singly linked list, reverse the list, and return its head.

Examples:
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input:  head = [1,2]
Output: [2,1]

Input:  head = []
Output: []
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Definition for singly-linked list.
from ds_utils.single_linked_list import ListNode


# Utility functions for testing
def from_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # TODO: Implement your solution here
        return head


# ---------------- TESTING ENVIRONMENT ----------------
def run_test(test_id, input_list, expected_list):
    head = from_list(input_list)
    result_head = Solution().reverseList(head)
    actual_list = to_list(result_head) if result_head else []
    correct = (actual_list == expected_list)

    print(f"Test {test_id}:")
    print(f"  Input:     {input_list}")
    print(f"  Expected:  {expected_list}")
    print(f"  Actual:    {actual_list}")
    print(f"  Result:    {'✅ Correct' if correct else '❌ Incorrect'}\n")
    return correct


if __name__ == "__main__":
    total, passed = 0, 0

    # Test cases (separated, not packed in one array)
    total += 1; passed += run_test(1, [1,2,3,4,5], [5,4,3,2,1])
    total += 1; passed += run_test(2, [1,2], [2,1])
    total += 1; passed += run_test(3, [], [])
    total += 1; passed += run_test(4, [1], [1])
    total += 1; passed += run_test(5, [1,2,3], [3,2,1])

    print("Summary:")
    print(f"  Passed {passed}/{total} tests")
    if passed == total:
        print("🎉 Awesome! All tests passed. Keep it up!")
    else:
        print("💡 Some tests failed. Debug and try again!")
