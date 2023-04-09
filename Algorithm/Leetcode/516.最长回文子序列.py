#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (51.41%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 27.6K
# Testcase Example:  '"bbbab"'
#
# 给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
#
# 示例 1:
# 输入:
#
#
# "bbbab"
#
#
# 输出:
#
#
# 4
#
#
# 一个可能的最长回文子序列为 "bbbb"。
#
# 示例 2:
# 输入:
#
#
# "cbbd"
#
#
# 输出:
#
#
# 2
#
#
# 一个可能的最长回文子序列为 "bb"。
#
#

# @lc code=start


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        # 反向遍历
        for i in range(n - 2, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][-1]

# @lc code=end
