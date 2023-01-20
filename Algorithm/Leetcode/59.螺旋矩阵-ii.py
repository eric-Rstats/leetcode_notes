#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n - 1, 0, n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res


# @lc code=end
