#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}  # 存储出现次数,第一次,第二次出现index

        for i, num in enumerate(nums):
            if num in d:
                d[num][0] += 1
                d[num][2] = i
            else:
                d[num] = [1, i, i]

        maxLen, minLen = 0, 0
        for cnt, left, right in d.values():
            if maxLen < cnt:
                maxLen = cnt
                minLen = right - left + 1
            elif maxLen == cnt:
                if minLen > (span := right - left + 1):
                    # 使用海象运算符，内存节省了一部分
                    minLen = span

        return minLen


# @lc code=end
