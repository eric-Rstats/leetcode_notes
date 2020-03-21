#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.44%)
# Likes:    568
# Dislikes: 0
# Total Accepted:    90.3K
# Total Submissions: 121.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        flag = [0] * len(nums)

        def drawback(nums, path):
            if len(nums) == len(path):
                result.append(path.copy())
                return

            for i, num in enumerate(nums):
                if flag[i] == 0:
                    flag[i] = 1
                    path.append(num)
                    drawback(nums, path)
                    flag[i] = 0
                    path.pop()
        drawback(nums, [])
        return result

# @lc code=end
