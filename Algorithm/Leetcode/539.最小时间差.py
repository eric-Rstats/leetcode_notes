#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = float("inf")
        t0Minutes = self.getMinutes(timePoints[0])
        preMinutes = t0Minutes
        for i in range(1, len(timePoints)):
            curminutes = self.getMinutes(timePoints[i])
            ans = min(ans, curminutes - preMinutes)
            preMinutes = curminutes
        ans = min(ans, t0Minutes + 1440 - preMinutes)

        return ans

    def getMinutes(self, t: str) -> int:
        return (
            ((ord(t[0]) - ord("0")) * 10 + ord(t[1]) - ord("0")) * 60
            + (ord(t[3]) - ord("0")) * 10
            + ord(t[4])
            - ord("0")
        )


# @lc code=end
