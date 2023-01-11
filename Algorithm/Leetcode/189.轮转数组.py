#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # # 版本1：类似迭代的方法
        # def reverse(nums, start, end):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1
        #     return nums

        # n = len(nums)
        # k %= n
        # reverse(nums, 0, n - 1)  # 先全部颠倒
        # reverse(nums, 0, k - 1)  # 再颠倒1-k
        # reverse(nums, k, n - 1)  # 颠倒剩下的部分

        # return nums

        # 版本2:利用切片
        n = len(nums)
        if k := k % n:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
        return nums


# @lc code=end
