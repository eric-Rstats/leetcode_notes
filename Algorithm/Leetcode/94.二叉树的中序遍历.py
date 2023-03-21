#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 版本1
        # result = []
        # def travel(root):
        #     if not root: return
        #     travel(root.left)
        #     result.append(root.val)
        #     travel(root.right)

        # travel(root)
        # return result

        # 版本2：迭代版本
        # if not root:
        #     return []
        # res = []
        # stack = []
        # cur = root
        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     else:
        #         cur = stack.pop()
        #         res.append(cur.val)
        #         cur = cur.right
        # return res

        # 版本3:通用的迭代,用null表示标记
        res = []
        stack = []
        if root:
            stack = [root]
        while stack:
            cur = stack.pop()  # 栈顶
            if cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)
            else:
                # 当栈顶为空时，开始出栈
                res.append(stack.pop().val)
        return res

        # @lc code=end
