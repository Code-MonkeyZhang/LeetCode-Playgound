
"""
LeetCode 707 — Design Linked List
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ds_utils.single_linked_list import ListNode

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0, next = None)
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
        
        if self.head == None:
            return -1 

        if index < 0 or index >= self.size:
            return -1
        
        current_node = self.head.next
        for _ in range(index):
            current_node = current_node.next

        return current_node.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val=val)


    """
    在第index个Node之前添加一个Node
    edge cases:
    - 如果List本身是空的, return
    - 如果index越界, return
    """
    def addAtIndex(self, index: int, val: int) -> None:
        if self.head == None:
            return

        if index < 0 or index > self.size:
            return
        
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        new_node = ListNode(val=val, next=prev_node.next)
        prev_node.next = new_node

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
        if self.head == None:
            return

        if index < 0 or index >= self.size:
            return
        
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        prev_node.next = prev_node.next.next
        self.size -= 1
