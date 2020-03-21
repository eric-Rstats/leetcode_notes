#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
# https://leetcode-cn.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (46.31%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 10K
# Testcase Example:  '[4,6,7,7]'
#
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例:
#
#
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
#
# 说明:
#
#
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
#
#
#

# @lc code=start


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def helper(start, nums, path):
            d = {}
            if len(path) >= 2:
                result.append(path.copy())
            if len(path) == n:
                return

            for i in range(start, n):
                if d.get(nums[i], 0):
                    continue
                if len(path) == 0 or nums[i] >= path[-1]:
                    d[nums[i]] = 1
                    path.append(nums[i])
                    helper(i + 1, nums, path)
                    path.pop()

        helper(0, nums, [])
        return result


# @lc code=end
