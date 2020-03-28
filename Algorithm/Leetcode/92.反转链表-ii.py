#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (49.52%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 83.4K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


""" class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverseN(head, n):
            if n == 1:
                return head
            last = reverseN(head.next, n - 1)
            successor = head.next.next
            head.next.next = head
            head.next = successor
            return last

        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head """


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        for i in range(m - 1):
            pre = pre.next

        start = pre.next
        tail = start.next  # 待变动插入的节点

        for i in range(n - m):
            start.next = tail.next
            pre.next = tail
            tail.next = start
            tail = start.next
        return dummy.next
# @lc code=end
