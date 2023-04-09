#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
# https://leetcode.cn/problems/distinct-subsequences/description/
#
# algorithms
# Hard (52.34%)
# Likes:    989
# Dislikes: 0
# Total Accepted:    130.5K
# Total Submissions: 249.7K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
# 
# 题目数据保证答案符合 32 位带符号整数范围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
# 
# 示例 2：
# 
# 
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length, t.length <= 1000
# s 和 t 由英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # 初始化细节
        for i in range(m):
            dp[i][0] = 1 # 可以首元素不取，也能认为匹配到
        for i in range(1, n):
            dp[0][i] = 0 

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # 也可以不用这个元素来匹配,需要累积可能性
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# @lc code=end

