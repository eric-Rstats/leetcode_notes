#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#

# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = Counter(s)
        cnt = Counter(target)
        res = inf
        for k, v in cnt.items():
            res = min(res, d[k] // v)
            if res == 0:
                return 0
        return res


# @lc code=end
