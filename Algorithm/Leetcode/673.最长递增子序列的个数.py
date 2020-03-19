#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (34.68%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 18.2K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#
#
# 示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
#
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
#
#

# @lc code=start


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp_length = [1 for _ in range(n)]  # 以i结尾的最长序列长度
        dp_count = [1 for _ in range(n)]  # 以i结尾的最长递增序列的个数

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp_length[j] >= dp_length[i]:
                        dp_length[i] = dp_length[j]+1
                        dp_count[i] = dp_count[j]
                    elif dp_length[j] + 1 == dp_length[i]:
                        dp_count[i] += dp_count[j]

        res = max(dp_length)
        return sum([dp_count[i] for i in range(n) if dp_length[i] == res])

# @lc code=end
