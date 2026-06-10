import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"
spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def test_basic_flow():
    my = mod.MyLinkedList()
    my.addAtHead(1)
    my.addAtTail(3)
    my.addAtIndex(1, 2)
    assert my.get(1) == 2
    my.deleteAtIndex(1)
    assert my.get(1) == 3


def test_get_on_empty():
    my = mod.MyLinkedList()
    assert my.get(0) == -1
    assert my.get(5) == -1


def test_add_at_index_zero():
    my = mod.MyLinkedList()
    my.addAtTail(2)
    my.addAtIndex(0, 1)
    assert my.get(0) == 1
    assert my.get(1) == 2


def test_add_at_index_len():
    my = mod.MyLinkedList()
    my.addAtHead(1)
    my.addAtIndex(1, 2)
    assert my.get(0) == 1
    assert my.get(1) == 2


def test_add_at_index_beyond_len():
    my = mod.MyLinkedList()
    my.addAtIndex(2, 3)
    assert my.get(0) == -1


def test_delete_head():
    my = mod.MyLinkedList()
    my.addAtHead(1)
    my.addAtHead(2)
    my.deleteAtIndex(0)
    assert my.get(0) == 1


def test_mixed_ops():
    my = mod.MyLinkedList()
    my.addAtHead(7)
    my.addAtHead(2)
    my.addAtHead(1)
    my.addAtIndex(3, 0)
    my.deleteAtIndex(2)
    my.addAtHead(6)
    my.addAtTail(4)
    assert my.get(4) == 4
    my.addAtHead(4)
    my.addAtIndex(5, 0)
    my.addAtHead(6)


test_basic_flow()
test_get_on_empty()
test_add_at_index_zero()
test_add_at_index_len()
test_add_at_index_beyond_len()
test_delete_head()
test_mixed_ops()

print("All tests passed!")
