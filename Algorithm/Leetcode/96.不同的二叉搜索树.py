#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode.cn/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (70.86%)
# Likes:    2182
# Dislikes: 0
# Total Accepted:    351.2K
# Total Submissions: 495.7K
# Testcase Example:  '3'
#
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
# @lc code=end

