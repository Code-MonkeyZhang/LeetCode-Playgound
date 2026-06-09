// LeetCode 707 — Design Linked List

class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

class MyLinkedList {
  constructor() {
    this.head = new ListNode(); // dummy head
    this.size = 0;
  }

  get(index) {
    if (index < 0 || index >= this.size) return -1;
    let cur = this.head.next;
    for (let i = 0; i < index; i++) cur = cur.next;
    return cur.val;
  }

  addAtHead(val) {
    this.addAtIndex(0, val);
  }

  addAtTail(val) {
    this.addAtIndex(this.size, val);
  }

  addAtIndex(index, val) {
    if (index < 0 || index > this.size) return;
    let prev = this.head;
    for (let i = 0; i < index; i++) prev = prev.next;
    prev.next = new ListNode(val, prev.next);
    this.size++;
  }

  deleteAtIndex(index) {
    if (index < 0 || index >= this.size) return;
    let prev = this.head;
    for (let i = 0; i < index; i++) prev = prev.next;
    prev.next = prev.next.next;
    this.size--;
  }
}

export { ListNode, MyLinkedList };
