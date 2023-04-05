#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (44.47%)
# Likes:    915
# Dislikes: 0
# Total Accepted:    178.8K
# Total Submissions: 400.1K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 示例 2：
# 
# 
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
# ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2*k+1)] for _ in range(n)]

        for i in range(1, 2*k, 2):
            dp[0][i] = -prices[0]

        # 单数表示此时买入, 双数表示此时售空
        for i in range(1, n):
            for j in range(0, 2*k-1, 2):
                # 单数
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j]-prices[i])
                # 双数
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1]+prices[i])
        return dp[-1][2*k]



# @lc code=end

