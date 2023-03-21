#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # from collections import deque
        # result = []
        # if not root:
        #     return []
        # que = deque([root])
        # while que:
        #     size = len(que)
        #     res = []

        #     for _ in range(size):
        #         cur = que.popleft()
        #         res.append(cur.val)
        #         if cur.left:
        #             que.append(cur.left)
        #         if cur.right:
        #             que.append(cur.right)
        #     result.append(res)
        # return result
        # 版本2: 递归法
        res = []

        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([])  # start the current depth
            res[depth].append(root.val)  # fulfil the current depth
            if root.left:
                # process child nodes for the next depth
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        helper(root, 0)
        return res


# @lc code=end
