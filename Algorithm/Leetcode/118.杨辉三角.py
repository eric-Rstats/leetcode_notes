#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        i = 0
        while i < numRows:
            row = []
            j = 0
            while j < i + 1:
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j - 1] + res[i - 1][j])
                j += 1
            res.append(row)
            i += 1
        return res


# @lc code=end
