#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#
# https://leetcode.cn/problems/maximum-erasure-value/description/
#
# algorithms
# Medium (51.64%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 25.5K
# Testcase Example:  '[4,2,4,5,6]'
#
# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
# 
# 返回 只删除一个 子数组可获得的 最大得分 。
# 
# 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [4,2,4,5,6]
# 输出：17
# 解释：最优子数组是 [2,4,5,6]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,2,1,2,5,2,1,2,5]
# 输出：8
# 解释：最优子数组是 [5,2,1] 或 [1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums) # 窗口长度为n-1
        left, result, total = 0, 0, 0
        hashmap = {}
        for right in range(n):
            tail = nums[right]
            total += tail
            hashmap[tail] = hashmap.get(tail, 0) + 1

            if right - left + 1 == len(hashmap):
                result = max(result, total)
            while right - left + 1 > len(hashmap):
                head = nums[left]
                hashmap[head] -= 1
                total -= head
                if hashmap[head] == 0:
                    del hashmap[head]
                left += 1
        return result
# @lc code=end

