#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        if not root1:
            return root2
        if not root2:
            return root1
        # 迭代法
        # que = deque()
        # que.append(root1)
        # que.append(root2)
        # while que:
        #     node1 = que.popleft()
        #     node2 = que.popleft()
        #     if node1.left and node2.left:
        #         que.append(node1.left)
        #         que.append(node2.left)
        #     if node1.right and node2.right:
        #         que.append(node1.right)
        #         que.append(node2.right)
        #     node1.val += node2.val
        #     if not node1.left and node2.left:
        #         node1.left = node2.left
        #     if not node1.right and node2.right:
        #         node1.right = node2.right
        # return root1
        
        # 递归
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
        

        # @lc code=end
