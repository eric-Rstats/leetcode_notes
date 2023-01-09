#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 二分法
        # citations.sort()
        l, r = 0, len(citations)

        def scan(x):
            # h指数的定义
            return sum([1 for c in citations if c >= x])

        while l <= r:
            mid = (l + r) // 2
            if scan(mid) >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r


# @lc code=end
