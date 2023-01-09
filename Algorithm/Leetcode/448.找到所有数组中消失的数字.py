#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 不使用哈希表的话,可以采取交换元素的方式
        res = []
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)

        return res


# @lc code=end
