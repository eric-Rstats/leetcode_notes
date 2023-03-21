#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                helper(root.left, depth+1)
            if root.right:
                helper(root.right, depth+1)
        helper(root, 0)
        res.reverse()
        return res
# @lc code=end
