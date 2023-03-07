#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = Counter(magazine)
        for x in ransomNote:
            if map.get(x, 0) > 0:
                map[x] -= 1
                continue
            if x not in map or map[x] == 0:
                return False
        return True
# @lc code=end
