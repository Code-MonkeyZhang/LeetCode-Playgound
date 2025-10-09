import sys
from pathlib import Path
import importlib.util

# 动态导入 linked-list.py（因为文件名包含连字符）
spec = importlib.util.spec_from_file_location(
    "linked_list",
    Path(__file__).parent / "linked-list.py"
)
linked_list_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(linked_list_module)

LinkedList = linked_list_module.LinkedList
ListNode = linked_list_module.ListNode


def test_basic_operations():
    """测试基本的链表操作"""
    print("测试基本操作...")

    ll = LinkedList()

    # 测试在空链表中获取
    assert ll.get(0) == -1, "空链表应该返回 -1"

    # 测试 addAtHead
    ll.addAtHead(1)
    assert ll.get(0) == 1, "头部插入后应该能获取到值"
    assert ll.size == 1, "大小应该为 1"

    # 测试 addAtTail
    ll.addAtTail(3)
    assert ll.get(1) == 3, "尾部插入后应该能获取到值"
    assert ll.size == 2, "大小应该为 2"

    # 测试 addAtIndex
    ll.addAtIndex(1, 2)
    assert ll.get(1) == 2, "在索引 1 插入后应该能获取到值"
    assert ll.get(0) == 1, "原来的头部应该还在"
    assert ll.get(2) == 3, "原来的尾部应该移到索引 2"
    assert ll.size == 3, "大小应该为 3"

    print("✓ 基本操作测试通过")


def test_delete_operations():
    """测试删除操作"""
    print("测试删除操作...")

    ll = LinkedList()
    ll.addAtHead(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    # 链表: 1 -> 2 -> 3 -> 4

    # 删除中间节点
    ll.deleteAtIndex(1)
    assert ll.get(0) == 1, "删除后头部不变"
    assert ll.get(1) == 3, "索引 1 应该是 3"
    assert ll.get(2) == 4, "索引 2 应该是 4"
    assert ll.size == 3, "删除后大小应该为 3"

    # 删除头部
    ll.deleteAtIndex(0)
    assert ll.get(0) == 3, "删除头部后，新头部应该是 3"
    assert ll.size == 2, "大小应该为 2"

    # 删除尾部
    ll.deleteAtIndex(1)
    assert ll.get(0) == 3, "只剩一个元素 3"
    assert ll.get(1) == -1, "索引 1 应该无效"
    assert ll.size == 1, "大小应该为 1"

    print("✓ 删除操作测试通过")


def test_edge_cases():
    """测试边界情况"""
    print("测试边界情况...")

    ll = LinkedList()

    # 测试负数索引
    assert ll.get(-1) == -1, "负数索引应该返回 -1"

    # 测试越界索引
    ll.addAtHead(1)
    assert ll.get(5) == -1, "越界索引应该返回 -1"

    # 测试在链表末尾插入（index == size）
    ll.addAtIndex(1, 2)
    assert ll.get(1) == 2, "在末尾插入应该成功"
    assert ll.size == 2, "大小应该为 2"

    # 测试异常情况
    try:
        ll.addAtIndex(10, 5)
        assert False, "应该抛出 IndexError"
    except IndexError:
        pass

    try:
        ll.deleteAtIndex(10)
        assert False, "应该抛出 IndexError"
    except IndexError:
        pass

    try:
        ll.deleteAtIndex(-1)
        assert False, "应该抛出 IndexError"
    except IndexError:
        pass

    print("✓ 边界情况测试通过")


def test_complex_scenario():
    """测试复杂场景（类似 LeetCode 707）"""
    print("测试复杂场景...")

    ll = LinkedList()

    ll.addAtHead(7)
    ll.addAtHead(2)
    ll.addAtHead(1)
    # 链表: 1 -> 2 -> 7

    ll.addAtIndex(3, 0)
    # 链表: 1 -> 2 -> 7 -> 0

    ll.deleteAtIndex(2)
    # 链表: 1 -> 2 -> 0

    ll.addAtHead(6)
    # 链表: 6 -> 1 -> 2 -> 0

    ll.addAtTail(4)
    # 链表: 6 -> 1 -> 2 -> 0 -> 4

    assert ll.get(4) == 4, "索引 4 应该是 4"

    ll.addAtHead(4)
    # 链表: 4 -> 6 -> 1 -> 2 -> 0 -> 4

    ll.addAtIndex(5, 0)
    # 链表: 4 -> 6 -> 1 -> 2 -> 0 -> 0 -> 4

    ll.addAtHead(6)
    # 链表: 6 -> 4 -> 6 -> 1 -> 2 -> 0 -> 0 -> 4

    assert ll.size == 8, "最终大小应该为 8"
    assert ll.get(0) == 6, "索引 0 应该是 6"
    assert ll.get(7) == 4, "索引 7 应该是 4"

    print("✓ 复杂场景测试通过")


def print_linked_list(ll: LinkedList):
    """打印链表内容（用于调试）"""
    if ll.size == 0:
        print("链表为空")
        return

    values = []
    for i in range(ll.size):
        values.append(str(ll.get(i)))
    print(" -> ".join(values))


if __name__ == "__main__":
    print("=" * 50)
    print("开始测试 LinkedList 类")
    print("=" * 50)

    try:
        test_basic_operations()
        test_delete_operations()
        test_edge_cases()
        test_complex_scenario()

        print("=" * 50)
        print("✅ 所有测试通过！")
        print("=" * 50)
    except AssertionError as e:
        print(f"❌ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
