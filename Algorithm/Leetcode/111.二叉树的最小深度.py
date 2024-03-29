#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (41.83%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    61.5K
# Total Submissions: 147K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        # 版本1:递归
        # if not root:
        #     return 0
        # if not root.left:
        #     return self.minDepth(root.right) + 1
        # if not root.right:
        #     return self.minDepth(root.left) + 1
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # 版本2:迭代
        if not root:
            return 0
        from collections import deque
        que = deque([root])
        depth = 0
        while que:
            size = len(que)
            depth += 1
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if not node.left and not node.right:
                    return depth
        return depth
# @lc code=end
