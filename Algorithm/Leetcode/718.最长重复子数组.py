#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (57.04%)
# Likes:    875
# Dislikes: 0
# Total Accepted:    175.5K
# Total Submissions: 307.7K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        result = 0
        for right in range(len())
# @lc code=end

