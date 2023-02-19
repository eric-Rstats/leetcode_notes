#
# @lc app=leetcode.cn id=962 lang=python3
#
# [962] 最大宽度坡
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        st = [0]
        for i, item in enumerate(nums):
            if i > 0 and item < nums[st[-1]]:
                st.append(i)
        res = 0
        for i in range(n - 1, 0, -1):
            while st and nums[i] >= nums[st[-1]]:
                res = max(res, i - st.pop())

        return res


# @lc code=end
