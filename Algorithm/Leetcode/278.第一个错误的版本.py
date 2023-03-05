#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            is_pick = isBadVersion(mid)
            if is_pick:
                right = mid - 1
            else:
                left = mid + 1

        return left


# @lc code=end
