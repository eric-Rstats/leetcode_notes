#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        n = len(nums)
        for i in range(n):
            if i <= max_index:
                max_index = max(max_index, i+nums[i])
                if max_index >= n - 1:
                    return True
            else:  # 不可能对的时候,break出来
                break
        return False
# @lc code=end
