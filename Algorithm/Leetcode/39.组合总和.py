#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.59%)
# Likes:    560
# Dislikes: 0
# Total Accepted:    73.7K
# Total Submissions: 107.5K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def drawback(candidates, start, target, path):
            if target == 0:
                result.append(path.copy())

            for i in range(start, len(candidates)):
                residus = target - candidates[i]
                if residus < 0:
                    break
                path.append(candidates[i])
                drawback(candidates, i, residus, path)
                path.pop()
        drawback(candidates, 0, target, [])
        return result

# @lc code=end
