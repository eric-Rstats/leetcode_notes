#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " ") and s[i] != " ":
                res += 1
        return res


# @lc code=end
