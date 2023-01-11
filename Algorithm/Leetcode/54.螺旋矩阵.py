#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # 版本1:削苹果方式
        # res = []
        # while matrix:
        #     res += matrix.pop(0)
        #     matrix = list(zip(*matrix))[::-1]
        # return res

        # 版本2:顺序遍历

        def circle(matrix, x1, y1, x2, y2, res):
            if x2 < x1 or y2 < y1:
                return -1
            if x1 == x2:
                for i in range(y1, y2 + 1):
                    res.append(matrix[x1][i])
                return res
            if y1 == y2:
                for i in range(x1, x2 + 1):
                    res.append(matrix[i][y2])
                return res

            for i in range(y1, y2):
                res.append(matrix[x1][i])
            for i in range(x1, x2):
                res.append(matrix[i][y2])
            for i in range(y2, y1, -1):
                res.append(matrix[x2][i])
            for i in range(x2, x1, -1):
                res.append(matrix[i][y1])
            return circle(matrix, x1 + 1, y1 + 1, x2 - 1, y2 - 1, res)

        res = []
        m = len(matrix)
        n = len(matrix[0])
        circle(matrix, 0, 0, m - 1, n - 1, res)

        return res


# @lc code=end
