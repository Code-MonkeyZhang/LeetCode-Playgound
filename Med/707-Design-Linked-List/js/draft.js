// LeetCode 707 — 设计链表
//
// 题目描述：设计链表的实现。你可以选择使用单链表或者双链表。
// 单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。
//
// 需要实现以下方法：
// - get(index)：获取链表中第 index 个节点的值。如果索引无效，返回 -1。
// - addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。
// - addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
// - addAtIndex(index, val)：在链表中的第 index 个节点之前添加值为 val 的节点。
// - deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
//
// 示例：
// linkedList.addAtHead(1);
// linkedList.addAtTail(3);
// linkedList.addAtIndex(1, 2);  // 链表变为 1->2->3
// linkedList.get(1);            // 返回 2
// linkedList.deleteAtIndex(1);  // 现在链表是 1->3
// linkedList.get(1);            // 返回 3

class MyLinkedList {
  constructor() {}

  get(index) {
    return -1;
  }

  addAtHead(val) {}

  addAtTail(val) {}

  addAtIndex(index, val) {}

  deleteAtIndex(index) {}
}

export { MyLinkedList };

if (import.meta.main) {
  await import("./test.js");
}
