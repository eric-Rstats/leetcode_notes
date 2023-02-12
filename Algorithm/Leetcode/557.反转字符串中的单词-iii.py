#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split()
        res = ""
        for s in string_list:
            res += s[::-1] + " "
        return res[:-1]


# @lc code=end
