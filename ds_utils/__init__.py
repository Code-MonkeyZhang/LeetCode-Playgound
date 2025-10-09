"""
ds_utils - 数据结构工具包
包含常用的数据结构实现，如链表、二叉树等。
"""

import importlib.util
from pathlib import Path

# 动态导入 single-linked-list.py（因为文件名包含连字符）
_spec = importlib.util.spec_from_file_location(
    "single_linked_list",
    Path(__file__).parent / "single-linked-list.py"
)
_single_linked_list = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_single_linked_list)

# 导出单链表相关类
ListNode = _single_linked_list.ListNode
LinkedList = _single_linked_list.LinkedList

__all__ = ['ListNode', 'LinkedList']
