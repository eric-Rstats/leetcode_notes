#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i in range(1, len(prices)):
        #     res += max(prices[i]-prices[i-1], 0)
        # return res

        # n = len(prices)
        # dp = [[0] * 2 for _ in range(2)]
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0
        # for i in range(1, n):
        #     dp[i % 2][0] = max(dp[(i-1) % 2][0], dp[(i-1)%2][1] - prices[i])
        #     dp[i % 2][1] = max(dp[(i-1) % 2][1], dp[(i-1)%2][0] + prices[i])
        # return dp[(n-1) % 2][-1]


        n = len(prices)
        hold = -prices[0]
        sell = 0
        for i in range(1, n):
            hold = max(hold, sell  - prices[i]) # 当前持有(上一次卖掉,本次购入;或者上次购入,这次保持不变)
            sell = max(sell, hold + prices[i]) # 当前售出(上次售出,这次不变;或者上次购入,这次卖出)
        return sell
# @lc code=end
