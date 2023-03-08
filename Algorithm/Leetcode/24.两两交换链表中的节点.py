#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy

        while pre.next and pre.next.next:
            cur = pre.next
            post = cur.next

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return dummy.next
# @lc code=end
