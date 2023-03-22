#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (67.75%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    17.2K
# Total Submissions: 25.4K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
# h 层，则该层包含 1~ 2^h 个节点。
#
# 示例:
#
# 输入:
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
#
# 输出: 6
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
    def countNodes(self, root: TreeNode) -> int:
        # hl, hr = 0, 0
        # left, right = root, root

        # while left:
        #     left = left.left
        #     hl += 1

        # while right:
        #     right = right.right
        #     hr += 1

        # if hl == hr:
        #     # 如果此次迭代左右子树高度一样，那么实际上是满二叉树
        #     return 2 ** hl - 1
        # else:
        #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        if not root:
            return 0
        from collections import deque
        que = deque([root])
        cnt = 0
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                cnt += 1

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return cnt
# @lc code=end
