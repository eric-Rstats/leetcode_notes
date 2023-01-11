#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sum_nums = [0]
        for i in range(n):
            self.sum_nums.append(self.sum_nums[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_nums[right + 1] - self.sum_nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
