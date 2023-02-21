#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        left, right = 0, 0
        while left < m and right < n:
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == m


# @lc code=end
