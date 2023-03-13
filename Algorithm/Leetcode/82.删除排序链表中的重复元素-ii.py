#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val != cur.next.next.val:
                cur = cur.next
            else:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
        return dummy.next


# @lc code=end
