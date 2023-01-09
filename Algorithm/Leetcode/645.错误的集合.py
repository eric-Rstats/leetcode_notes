#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 普通方法,用字典存储出现过的元素;
        # 出现过2次的为重复,没出现过的是丢失的
        s1, s2 = 0, 0
        n = len(nums)
        cnt = [0 for i in range(n)]

        for num in nums:
            cnt[num-1] += 1
        for i, num in enumerate(cnt):
            if num == 0:
                s2 = i+1
            if num == 2:
                s1 = i+1

        return [s1, s2]


# @lc code=end
