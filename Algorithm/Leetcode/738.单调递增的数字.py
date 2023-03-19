#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        length = len(n)

        for i in range(length-2, -1, -1):
            if n[i] > n[i+1]:
                n[i+1:] = "9" * (length - i - 1)
                n[i] = str(int(n[i]) - 1)
        return int("".join(n))
# @lc code=end
