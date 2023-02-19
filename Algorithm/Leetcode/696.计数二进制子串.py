#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)  # 字符串长度
        res = 0
        seq0, freq = 0, 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                freq += 1
            else:
                res += min(seq0, freq)
                seq0 = freq
                freq = 1
        res += min(seq0, freq)
        return res


# @lc code=end
