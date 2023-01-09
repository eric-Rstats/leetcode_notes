#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 其实相当于看是否存在n-1长度的非递减数列(但是可跳跃)

        n = len(nums)
        count = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                # 出现递减情况
                count += 1
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return count <= 1


# @lc code=end
