#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (57.63%)
# Likes:    246
# Dislikes: 0
# Total Accepted:    44.8K
# Total Submissions: 77.8K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        flag = [0] * len(nums)

        def drawback(nums, path):
            if len(nums) == len(path):
                result.append(path.copy())
                return

            for i, num in enumerate(nums):
                if flag[i] == 1:
                    continue
                if num == nums[i - 1] and i > 0 and flag[i - 1] == 0:
                    continue

                path.append(num)
                flag[i] = 1
                drawback(nums, path)
                flag[i] = 0
                path.pop()

        drawback(nums, [])
        return result

        # @lc code=end
