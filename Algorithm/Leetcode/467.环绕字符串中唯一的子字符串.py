#
# @lc app=leetcode.cn id=467 lang=python3
#
# [467] 环绕字符串中唯一的子字符串
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = collections.defaultdict(int)
        n = len(s)
        res = 0
        for i in range(n):
            if i > 0 and (
                ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == "a" and s[i - 1] == "z")
            ):
                res += 1
            else:
                res = 1
            count[s[i]] = max(count[s[i]], res)
        return sum(count.values())


# @lc code=end
