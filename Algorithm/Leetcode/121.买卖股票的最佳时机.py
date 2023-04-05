#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        # max_value = 0
        # min_value = inf
        # for item in prices:
        #     max_value = max(max_value, item-min_value)
        #     min_value = min(min_value, item)
        # return max_value

        # 动态规划
        hold, sell = -prices[0], 0 # 持有股票,销售股票

        for i in range(1, len(prices)):
            hold = max(hold, -prices[i])
            sell = max(sell, hold + prices[i])
        return sell



# @lc code=end
