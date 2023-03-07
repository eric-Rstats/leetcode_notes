#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}
        for i, item in enumerate(s):
            if item in char_map:
                char_map[item] = -1
            else:
                char_map[item] = i
        res = [v for k,v in char_map.items() if v!=-1]
        return -1 if not res else min(res)

# @lc code=end
