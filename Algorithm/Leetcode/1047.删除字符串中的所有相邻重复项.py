#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for item in s:
            if not res or item != res[-1]:
                res.append(item)
            else:
                res.pop()
        return "".join(res)

# @lc code=end
