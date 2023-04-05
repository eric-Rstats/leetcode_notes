#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (64.08%)
# Likes:    1466
# Dislikes: 0
# Total Accepted:    245.7K
# Total Submissions: 383.4K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
# 示例 2:
# 
# 
# 输入: prices = [1]
# 输出: 0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态1：持有股票
        # 状态2：保持无股票在手
        # 状态3: 今天卖出股票
        # 状态4: 冷冻期,则一定前一天卖出了股票
        # n = len(prices)
        # dp = [[0 for _ in range(4)] for _ in range(n)]
        # dp[0][0] = -prices[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][0], max(dp[i-1][1]-prices[i], dp[i-1][3]-prices[i]))
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][3])
        #     dp[i][2] = dp[i-1][0] + prices[i]
        #     dp[i][3] = dp[i-1][2]
        # return max(dp[-1])

        n = len(prices)
        if n < 2:
            return 0
        sell = [0] * n
        buy = [0] * n
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], buy[0]+prices[1])
        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2]-prices[i]) 
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        return max(sell[-1], sell[-2])



# @lc code=end

