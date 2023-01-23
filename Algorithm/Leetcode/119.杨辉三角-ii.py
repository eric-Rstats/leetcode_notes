#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0 for _ in range(rowIndex + 1)]
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row

        # res = []
        # i = 0
        # while i < rowIndex + 1:
        #     row = []
        #     j = 0
        #     while j < i + 1:
        #         if j == 0 or j == i:
        #             row.append(1)
        #         else:
        #             row.append(res[i - 1][j - 1] + res[i - 1][j])
        #         j += 1
        #     res.append(row)
        #     i += 1
        # return res[-1]


# @lc code=end
