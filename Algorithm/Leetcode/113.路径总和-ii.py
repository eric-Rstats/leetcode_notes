#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode.cn/problems/path-sum-ii/description/
#
# algorithms
# Medium (63.23%)
# Likes:    942
# Dislikes: 0
# Total Accepted:    334.3K
# Total Submissions: 528.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 
# 叶子节点 是指没有子节点的节点。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,2], targetSum = 0
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点总数在范围 [0, 5000] 内
# -1000 
# -1000 
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result, path = [], []
        def travel(cur, remain):

            if not cur.left and not cur.right:
                if remain == 0:
                    result.append(path[:])
                return
            
            if cur.left:
                path.append(cur.left.val)
                travel(cur.left, remain - cur.left.val)
                path.pop() 

            if cur.right:
                path.append(cur.right.val)
                travel(cur.right, remain - cur.right.val)
                path.pop()

        if not root:
            return []
        else:
            path.append(root.val)
            travel(root, targetSum - root.val)
            return result        
# @lc code=end

