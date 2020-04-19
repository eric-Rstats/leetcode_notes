#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (39.97%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    55.5K
# Total Submissions: 138.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 首先计算一下链表的长度
        def length(head):
            l = 0
            while head:
                head = head.next
                l += 1
            return l

        if not head or not head.next:
            return head

        # 真实需要移动的次数
        l = length(head)
        cnt = k % l

        cur = head
        for i in range(l - cnt - 1):
            cur = cur.next

        tail = cur
        while tail.next:
            tail = tail.next

        tail.next = head
        head = cur.next
        cur.next = None

        return head
# @lc code=end
