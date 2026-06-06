
"""
LeetCode 707 — Design Linked List (Test Harness)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import List, Tuple, Callable
import importlib.util, sys

_project_root = Path(__file__).resolve().parent.parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

_spec = importlib.util.spec_from_file_location(
    "solution",
    Path(__file__).parent / "707_Build_Linkedlist.py",
    submodule_search_locations=[],
)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["solution"] = _mod
_spec.loader.exec_module(_mod)
MyLinkedList = _mod.MyLinkedList

TestFunc = Callable[[], Tuple[str, List[int], List[int]]]

def _run_and_capture(ops: List[Tuple[str, tuple]]) -> List[int]:
    my = MyLinkedList()
    got = []
    for name, args in ops:
        if name == 'get':
            got.append(getattr(my, name)(*args))
        else:
            getattr(my, name)(*args)
    return got

def test_example_from_prompt() -> Tuple[str, List[int], List[int]]:
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
        ('addAtIndex', (0, 10)),
        ('get', (0,)),
    ]
    expected = [10]
    actual = _run_and_capture(ops)
    return ('addAtIndex(0, val) inserts at head', expected, actual)

def test_add_at_index_equal_len_appends() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (1,)),
        ('addAtTail', (3,)),
        ('addAtIndex', (2, 5)),
        ('get', (2,)),
    ]
    expected = [5]
    actual = _run_and_capture(ops)
    return ('addAtIndex(len, val) appends', expected, actual)

def test_add_at_index_greater_than_len_noop() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (7,)),
        ('addAtIndex', (5, 9)),
        ('get', (0,)),
        ('get', (1,)),
    ]
    expected = [7, -1]
    actual = _run_and_capture(ops)
    return ('addAtIndex(>len) does nothing', expected, actual)

def test_delete_head_and_then_gets() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (4,)),
        ('addAtTail', (5,)),
        ('deleteAtIndex', (0,)),
        ('get', (0,)),
        ('get', (1,)),
    ]
    expected = [5, -1]
    actual = _run_and_capture(ops)
    return ('deleteAtIndex on head', expected, actual)

def test_mixed_ops_small() -> Tuple[str, List[int], List[int]]:
    ops = [
        ('addAtHead', (1,)),
        ('addAtHead', (2,)),
        ('addAtTail', (3,)),
        ('addAtIndex', (1, 9)),
        ('get', (0,)),
        ('get', (1,)),
        ('get', (2,)),
        ('get', (3,)),
    ]
    expected = [2, 9, 1, 3]
    actual = _run_and_capture(ops)
    return ('Mixed operations', expected, actual)

TESTS: List[TestFunc] = [
    test_example_from_prompt,
    test_invalid_get_on_empty,
    test_add_at_index_zero_behaves_like_head,
    test_add_at_index_equal_len_appends,
    test_add_at_index_greater_than_len_noop,
    test_delete_head_and_then_gets,
    test_mixed_ops_small,
]

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

    print()
    print('=' * 60)
    print(f'SUMMARY: Passed {passed} / {total} tests.')
    if passed == total:
        print('Awesome job! All tests passed!')
    else:
        print('Keep going — fix your implementation and run again.')
    print('=' * 60)

if __name__ == '__main__':
    main()
