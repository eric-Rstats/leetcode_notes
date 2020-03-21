#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (70.41%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    16.1K
# Total Submissions: 22.9K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

# @lc code=start


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        flag = [0] * 9

        def drawback(k, target, path, curr):
            if len(path) == k and target == 0:
                result.append(path.copy())
                return

            for i in range(curr, 9):
                residual = target - i - 1
                if residual < 0:
                    break
                flag[i] = 1
                path.append(i+1)
                drawback(k, residual, path, i+1)
                path.pop()
                flag[i] = 0

        drawback(k, n, [], 0)
        return result
# @lc code=end
