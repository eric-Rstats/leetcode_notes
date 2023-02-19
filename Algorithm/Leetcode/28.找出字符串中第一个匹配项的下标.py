#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = self.get_next(needle)
        i = j = 0
        m, n = len(haystack), len(needle)
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == n:
            return i - j
        else:
            return -1

    def get_next(self, needle):
        res = [-1 for _ in range(len(needle))]
        i, j = 0, -1
        while i < len(needle) - 1:
            if j == -1 or needle[i] == needle[j]:
                j += 1
                i += 1
                res[i] = j
            else:
                j = res[j]
        return res


# @lc code=end
