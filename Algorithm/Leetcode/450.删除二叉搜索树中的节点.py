#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (39.03%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 26.2K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
#
#
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
#
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
#
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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def successor(cur):
            # 中序遍历的后续节点
            cur = cur.right
            while cur.left:
                cur = cur.left
            return cur

        def predecessor(cur):
            # 中序遍历的前序节点
            cur = cur.left
            while cur.right:
                cur = cur.right
            return cur

        def delete(cur, key):
            if not cur:
                return None
            if cur.val < key:
                cur.right = delete(cur.right, key)
            elif cur.val > key:
                cur.left = delete(cur.left, key)
            else:
                if not cur.left and not cur.right:
                    # 如果是叶子节点
                    cur = None
                elif cur.right:
                    cur.val = successor(cur).val
                    cur.right = delete(cur.right, cur.val)
                else:
                    cur.val = predecessor(cur).val
                    cur.left = delete(cur.left, cur.val)

            return cur

        return delete(root, key)


# @lc code=end
