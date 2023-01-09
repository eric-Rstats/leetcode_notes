#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#
# https://leetcode.cn/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (61.22%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    185.6K
# Total Submissions: 303.9K
# Testcase Example:  '[1,1,0,1,1,1]'
#


# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_item, n = 0, 0
        for num in nums:
            if num == 1:
                n += 1
            else:
                n = 0
            max_item = max(max_item, n)
        return max_item


# @lc code=end
