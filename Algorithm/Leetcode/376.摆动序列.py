#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre, cur, res = 0, 0, 1
        for i in range(len(nums)-1):
            cur = nums[i+1] - nums[i]
            if pre * cur <= 0 and cur != 0:
                res += 1
                pre = cur
        return res
# @lc code=end

