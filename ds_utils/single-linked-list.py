from turtle import heading
from typing import Optional


class ListNode:
    """单链表节点。

    Attributes:
        val (int): 节点存储的整数值。
        next (Optional['ListNode']): 指向链表中下一个节点的指针，如果是尾节点则为 None。
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        """初始化一个链表节点。

        Args:
            val: 要存储在节点中的值。
            next: 链表中的下一个节点。
        """
        self.val = val
        self.next = next


class LinkedList:
    """
    单链表实现

    Attributes:
        head (ListNode): 指向虚拟头节点的指针。
        size (int): 链表中存储的实际节点数量, 写的时候要注意更新
    """

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode(val=0, next=None)

    def get(self, index: int) -> int:
        """获取链表中第 index 个节点的值。

        如果索引无效，则返回 -1。

        Args:
            index: 要获取的节点的索引，从 0 开始。

        Returns:
            指定索引处节点的值，如果索引无效则返回 -1。
        """

        """
        Edge Cases:
            - 索引无效: index为负数, index越界
        思路: 从头到尾遍历到那个Node,然后取值
        """

        if index < 0 or index >= self.size:
            return -1

        # 开始遍历
        current_node = self.dummy_head
        for _ in range(index):
            current_node = current_node.next

        return current_node.next.val

    def addAtHead(self, val: int) -> None:
        """在链表的头部插入一个新节点。

        Args:
            val: 新节点的值。
        """
        """
        edge cases: 
        """
        new_node = ListNode(val=val, next=self.dummy_head.next)
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """在链表的末尾追加一个新节点。
        Edges:
            如果List是空的,等于addHead

        Args:
            val: 新节点的值。
        """

        # 遍历到结尾,然后添加
        current_node = self.dummy_head

        for _ in range(self.size):
            current_node = current_node.next

        new_node = ListNode(val=val, next=None)
        current_node.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """在链表的第 index 个节点之前插入一个新节点。

        如果 index 等于链表的长度，则该节点将追加到链表的末尾。
        如果 index 大于链表长度，则不会插入该节点。

        Args:
            index: 插入新节点的位置索引。
            val: 新节点的值。
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range of linked-list")

        # 思路: 遍历到前一个
        current_node = self.dummy_head
        for _ in range(index):
            current_node = current_node.next

        new_node = ListNode(val=val, next=current_node.next)
        current_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """如果索引有效，则删除链表中的第 index 个节点。

        Edges:
            - 不存在
            - 

        Args:
            index: 要删除的节点的索引。
        """

        # 思路: 遍历到index前一个, 连到下一个
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current_node = self.dummy_head

        for _ in range(index):
            current_node = current_node.next

        current_node.next = current_node.next.next
        self.size -= 1
