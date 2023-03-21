#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        min_value = inf
        for i, item in enumerate(prices):
            max_value = max(max_value, item-min_value)
            min_value = min(min_value, item)
        return max_value


# @lc code=end
