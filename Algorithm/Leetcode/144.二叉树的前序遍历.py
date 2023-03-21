#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        # def travel(root):
        #     if not root: return
        #     result.append(root.val)
        #     travel(root.left)
        #     travel(root.right)

        # travel(root)
        # return result

        # 迭代方式
        # if not root:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     cur = stack.pop()
        #     res.append(cur.val) # 中
        #     if cur.right:
        #         stack.append(cur.right)
        #     if cur.left:
        #         stack.append(cur.left)
        # return res

        # 版本3
        res = []
        stack = []
        if root:
            stack = [root]
        while stack:
            cur = stack.pop()  # 栈顶
            if cur:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                stack.append(cur)
                stack.append(None)
            else:
                # 当栈顶为空时，开始出栈
                res.append(stack.pop().val)
        return res
    # @lc code=end
