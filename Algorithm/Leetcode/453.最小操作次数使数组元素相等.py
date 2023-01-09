#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # n-1个都加1,相当于1个元素降低1
        min_item = min(nums)
        res = 0
        for num in nums:
            res += num - min_item
        return res


# @lc code=end
