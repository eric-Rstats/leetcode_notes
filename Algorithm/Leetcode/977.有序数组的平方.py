#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        res = [0] * n
        cur = n - 1
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                res[cur] = nums[right] ** 2
                right -= 1
            else:
                res[cur] = nums[left] ** 2
                left += 1

            cur -= 1
        return res

# @lc code=end
