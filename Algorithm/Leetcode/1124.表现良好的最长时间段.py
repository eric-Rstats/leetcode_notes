#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        n = len(hours)
        presum = [0]
        st = [0]
        for i, h in enumerate(hours):
            h = 1 if h > 8 else -1
            presum.append(h + presum[-1])
            if presum[-1] < presum[st[-1]]:
                st.append(i + 1)
        res = 0
        for j in range(n, 0, -1):
            while st and presum[j] > presum[st[-1]]:
                res = max(res, j - st.pop())

        return res


# @lc code=end
