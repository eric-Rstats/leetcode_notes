#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n_upper = sum([1 for _ in word if _.isupper()])
        n = len(word)

        if n == n_upper or n_upper == 0:
            return True
        elif n_upper == 1 and word[0].isupper():
            return True
        else:
            return False


# @lc code=end
