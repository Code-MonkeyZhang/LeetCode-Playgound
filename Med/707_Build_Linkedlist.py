
"""
LeetCode 707 — Design Linked List (Test Harness)
------------------------------------------------
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ds_utils.single_linked_list import ListNode

# =========================
# ===== USER — TODO =======
# =========================

class MyLinkedList:
    """
    Implement your linked list here.
    """

    def __init__(self):
        self.head = ListNode(0, next = None) # dummy head
        self.size = 0
    
    """
    给index,获取链表中下标为index的Node的值
    
    方法:
    - 从dummy开始遍历index次
    - 直到遍历到index所指的Node,返回那个数

    edge cases:
    - 如果是链表是空的 return -1
    - 如果index越界 return -1
    """
    def get(self, index: int) -> int:
        
        # 如果是链表是空的返回 -1
        if self.head == None:
            return -1 

        # 如果index无效返回 -1
        if index < 0 or index >= self.size:
            return -1
        
        # 从dummy之后的head开始遍历index次
        # 就能遍历到第index个
        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next

        return current_node.val


    """
    用addAtIndex函数统一实现
    """
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)


    """
    用addAtIndex函数统一实现
    """
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val=val)


    """
    在第index个Node之前添加一个Node
    edge cases:
    - 如果List本身是空的, return
    - 如果index越界, return
    """
    def addAtIndex(self, index: int, val: int) -> None:
        # if the List is empty, return
        if self.head == None:
            return

        # if index is invalid, return
        if index < 0 or index > self.size:
            return
        
        # 从dummy开始用for循环遍历到第index的前一个Node
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        # 插入ListNode
        new_node = ListNode(val=val, next=prev_node.next)
        prev_node.next = new_node

        # 维护size
        self.size += 1

        
    """
    删除指定index的Node

    edge cases:
    - 如果是0,直接删head

    正常:
    - 遍历到index-1个Node
    - 获取要删掉的node
    - 获取要删的node的next
    - 桥接

    """
    def deleteAtIndex(self, index: int) -> None:
        # if the List is empty, return
        if self.head == None:
            return

        # if index is invalid, return
        if index < 0 or index >= self.size:
            return
        
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        prev_node.next = prev_node.next.next
        self.size -= 1
    

# =========================
# ===== Test Harness ======
# =========================

from typing import List, Tuple, Callable

TestFunc = Callable[[], Tuple[str, List[int], List[int]]]
# Each test returns: (name, expected_outputs, actual_outputs)

def _run_and_capture(ops: List[Tuple[str, tuple]]) -> List[int]:
    """
    Execute a sequence of (method_name, args) on a new MyLinkedList.
    Only captures outputs from `get` operations in order.
    """
    my = MyLinkedList()
    got = []
    for name, args in ops:
        if name == 'get':
            got.append(getattr(my, name)(*args))
        else:
            getattr(my, name)(*args)
    return got

# ---- Individual, separated tests (easy to set breakpoints) ----

def test_example_from_prompt() -> Tuple[str, List[int], List[int]]:
    # From the problem statement example
    ops = [
        ('addAtHead', (1,)),
        ('addAtTail', (3,)),
        ('addAtIndex', (1, 2)),
        ('get', (1,)),
        ('deleteAtIndex', (1,)),
        ('get', (1,)),
    ]
    expected = [2, 3]
    actual = _run_and_capture(ops)
    return ('Example / Basic Flow', expected, actual)

def test_invalid_get_on_empty() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('get', (0,)),
        ('get', (5,)),
    ]
    expected = [-1, -1]
    actual = _run_and_capture(ops)
    return ('Invalid get on empty list', expected, actual)

def test_add_at_index_zero_behaves_like_head() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtIndex', (0, 10)),  # should insert at head
        ('get', (0,)),
    ]
    expected = [10]
    actual = _run_and_capture(ops)
    return ('addAtIndex(0, val) inserts at head', expected, actual)

def test_add_at_index_equal_len_appends() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (1,)),
        ('addAtTail', (3,)),
        ('addAtIndex', (2, 5)),   # index == length -> append
        ('get', (2,)),
    ]
    expected = [5]
    actual = _run_and_capture(ops)
    return ('addAtIndex(len, val) appends', expected, actual)

def test_add_at_index_greater_than_len_noop() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (7,)),
        ('addAtIndex', (5, 9)),   # > length -> no insert
        ('get', (0,)),
        ('get', (1,)),            # should be invalid
    ]
    expected = [7, -1]
    actual = _run_and_capture(ops)
    return ('addAtIndex(>len) does nothing', expected, actual)

def test_delete_head_and_then_gets() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (4,)),
        ('addAtTail', (5,)),
        ('deleteAtIndex', (0,)),  # delete head -> list: [5]
        ('get', (0,)),            # expect 5
        ('get', (1,)),            # expect -1
    ]
    expected = [5, -1]
    actual = _run_and_capture(ops)
    return ('deleteAtIndex on head', expected, actual)

def test_mixed_ops_small() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (1,)),
        ('addAtHead', (2,)),
        ('addAtTail', (3,)),
        ('addAtIndex', (1, 9)),  # list should become: 2,9,1,3
        ('get', (0,)),           # 2
        ('get', (1,)),           # 9
        ('get', (2,)),           # 1
        ('get', (3,)),           # 3
    ]
    expected = [2, 9, 1, 3]
    actual = _run_and_capture(ops)
    return ('Mixed operations', expected, actual)

# Collect all tests here
TESTS: List[TestFunc] = [
    test_example_from_prompt,
    test_invalid_get_on_empty,
    test_add_at_index_zero_behaves_like_head,
    test_add_at_index_equal_len_appends,
    test_add_at_index_greater_than_len_noop,
    test_delete_head_and_then_gets,
    test_mixed_ops_small,
]

# ------------- Runner -------------

def _print_header():
    line = '=' * 60
    print(line)
    print('LeetCode 707 — Design Linked List | Python Test Harness')
    print(line)
    print()

def _print_single_result(name: str, expected: List[int], actual: List[int]) -> bool:
    ok = (expected == actual)
    status = 'PASS' if ok else 'FAIL'
    print(f'[TEST] {name}')
    print(f'  Expected: {expected}')
    print(f'  Actual  : {actual}')
    print(f'  Result  : {status}')
    print('-' * 60)
    return ok

def main():
    _print_header()
    passed = 0
    total = len(TESTS)
    for test in TESTS:
        name, expected, actual = test()
        if _print_single_result(name, expected, actual):
            passed += 1

    # Summary
    print()
    print('=' * 60)
    print(f'SUMMARY: Passed {passed} / {total} tests.')
    if passed == total:
        print('Awesome job! All tests passed — keep up the momentum! 🚀')
    else:
        print('Keep going — fix your implementation and run again. You ve got this!')
    print('=' * 60)

if __name__ == '__main__':
    main()
