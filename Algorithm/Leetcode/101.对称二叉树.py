#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        #     # 1. 递归法
        #     if not root:
        #         return True
        #     return self.compare(root.left, root.right)

        # def compare(self, left, right):
        #     if not left and right:
        #         return False
        #     elif not right and left:
        #         return False
        #     elif not left and not right:
        #         return True
        #     elif left.val != right.val:
        #         return False

        #     flag1 = self.compare(left.left, right.right)
        #     flag2 = self.compare(left.right, right.left)
        #     return flag1 and flag2

        # 2. 使用队列(广度优先)
        # if not root:
        #     return True

        # from collections import deque
        # que = deque()
        # que.append(root.left)
        # que.append(root.right)
        # while que:
        #     left = que.popleft()  # 左
        #     right = que.popleft()  # 右

        #     if not left and not right:
        #         continue

        #     if not left or not right or left.val != right.val:
        #         return False

        #     que.append(left.left)
        #     que.append(right.right)
        #     que.append(left.right)
        #     que.append(right.left)
        # return True
        # 3. 层次遍历
        if not root:
            return True
        que = [root]
        while que:
            size = len(que)
            # 比较这一层是否对称
            left, right = 0, size-1
            while left <= right:
                if (not que[left] and que[right]) or (que[left] and not que[right]):
                    return False
                if que[left] and que[left].val != que[right].val:
                    return False

                left += 1
                right -= 1

            for i in range(size):
                if not que[i]:
                    continue
                que.append(que[i].left)
                que.append(que[i].right)
            que = que[size:]
        return True

        # @lc code=end
