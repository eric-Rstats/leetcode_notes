#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        for left in range(0, n, 2 * k):
            # 判断剩下的是否有k
            right = min(left + k - 1, n - 1)
            self.reverseString(s, left, right)
        return "".join(s)

    def reverseString(self, s: List[str], left: int, right: int) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# @lc code=end
