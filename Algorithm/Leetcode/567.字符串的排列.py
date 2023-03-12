#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = Counter(s1)
        n, m = len(s1), len(s2)
        window = {}
        left = 0
        for right in range(m):
            item = s2[right]
            window[item] = window.get(item, 0) + 1
            if window == needs:
                return True
            if right >= n - 1:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

        return False
            
# @lc code=end

