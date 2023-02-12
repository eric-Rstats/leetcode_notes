#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = x = 0

        for i in moves:
            if i == "U":
                y += 1
            if i == "D":
                y -= 1
            if i == "L":
                x -= 1
            if i == "R":
                x += 1
        return x == y == 0


# @lc code=end
