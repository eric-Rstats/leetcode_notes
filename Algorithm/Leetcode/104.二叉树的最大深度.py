#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (72.59%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    147.2K
# Total Submissions: 202.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最大深度 3 。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 版本1:递归法
        # if not root:
        #     return 0
        # else:
        #     left_depth = self.maxDepth(root.left)
        #     right_depth = self.maxDepth(root.right)
        #     return max(left_depth, right_depth) + 1
        # 版本2:层序遍历
        if not root:
            return 0
        from collections import deque
        que = deque([root])
        depth = 0
        while que:
            depth += 1
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return depth


# @lc code=end
