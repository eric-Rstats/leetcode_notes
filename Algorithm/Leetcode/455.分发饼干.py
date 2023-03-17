#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        res = 0
        # 优先匹配胃口小的
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:
                res += 1
        return res
# @lc code=end
