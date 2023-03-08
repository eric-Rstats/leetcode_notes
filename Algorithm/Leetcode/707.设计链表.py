#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head.next
        self.head.next = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return

        newnode = Node(val)
        cur = self.head
        for i in range(index):
            cur = cur.next
        newnode.next = cur.next
        cur.next = newnode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)
        # @lc code=end
