#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (39.08%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 92K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要
# 修改 数组以供接下来的操作使用。
# 
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 最长数组，等于sum-x
        nums_sum = sum(nums)
        n = len(nums)
        target = nums_sum - x
        if target < 0:
            return -1
        result, left, total = -1, 0, 0
        for right in range(n):
            total += nums[right]

            while total > target:
                total -= nums[left]
                left += 1
            if total == target:
                result = max(right-left+1, result)
        return -1 if result == - 1 else n - result
# @lc code=end

