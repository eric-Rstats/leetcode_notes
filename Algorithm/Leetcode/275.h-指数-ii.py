#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1

        # def scan(x):
        #     # h指数的定义
        #     return sum([1 for c in citations if c >= x])

        while l <= r:
            mid = (l + r) // 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return n - l


# @lc code=end
