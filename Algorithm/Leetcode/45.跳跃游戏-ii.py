#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        result, maxPos, end = 0, 0, 0
        n = len(nums)
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos, i+nums[i])
                if i == end:
                    result += 1
                    end = maxPos
        return result


# @lc code=end
