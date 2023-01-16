#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        presum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + arr[i - 1]
        res = 0
        for i in range(1, n + 1, 2):
            for j in range(0, n + 1 - i, 1):
                r = j + i - 1
                res += presum[r + 1] - presum[j]
        return res


# @lc code=end
