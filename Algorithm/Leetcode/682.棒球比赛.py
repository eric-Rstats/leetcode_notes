#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op == "C":
                res.pop()
            elif op == "D":
                res.append(res[-1] * 2)
            elif op == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))

        return sum(res)
# @lc code=end
