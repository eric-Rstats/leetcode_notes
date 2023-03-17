#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # 版本1: 贪心
        # res = -float('inf')
        # total = 0
        # for item in nums:
        #     total += item
        #     if total > res:
        #         res = total
        #     if total < 0:
        #         total = 0
        # return res

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            # 到i的最长数组,要么是连续，要么是从头开始累积
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i] > res:
                res = dp[i]

        return res

        # @lc code=end
