#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        cur = res = sum([i * num for i, num in enumerate(nums)])
        for i in range(1, n):
            cur = cur + total - n * nums[n - i]
            res = max(cur, res)

        return res


# @lc code=end
