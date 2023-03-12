#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (41.65%)
# Likes:    213
# Dislikes: 0
# Total Accepted:    32.4K
# Total Submissions: 77.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
#
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, total = 0, 0
        n = len(nums)
        result = n+1
        for right in range(n):
            total += nums[right]

            while total >= s:
                result = min(right-left+1, result)
                total -= nums[left]
                left += 1
        return 0 if result == n+1 else result


        # # 版本1:滑动窗口
        # left = right = total = 0
        # n = len(nums)
        # res = n + 1
        # while right < n:
        #     total += nums[right]
        #     while total >= s:
        #         res = min(res, right-left+1)
        #         total -= nums[left]
        #         left += 1
        #     right += 1
        # return 0 if res == n + 1 else res

        # 版本2: 前缀和+二分查找
        # def bisect_search(target, nums, l, r):
        #     while l < r:
        #         mid = (l + r) // 2
        #         if nums[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid
        #     return l if nums[l] >= target else -1

        # presum = [0]
        # n = len(nums)
        # res = n + 1
        # # 前缀和
        # for num in nums:
        #     presum.append(presum[-1] + num)
        # for i in range(1, n + 1):
        #     target = presum[i - 1] + s
        #     l, r = i, n
        #     while l < r:
        #         mid = (l + r) // 2
        #         if presum[mid] >= target:
        #             r = mid
        #         else:
        #             l = mid + 1
        #     if presum[l] >= target:
        #         # 可能没有搜寻到
        #         res = min(res, l - i + 1)
        # return res if res < n + 1 else 0

        # @lc code=end
