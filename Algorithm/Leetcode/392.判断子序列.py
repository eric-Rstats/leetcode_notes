#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # m, n = len(s), len(t)
        # left, right = 0, 0
        # while left < m and right < n:
        #     if s[left] == t[right]:
        #         left += 1
        #     right += 1
        # return left == m
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] == m


# @lc code=end
