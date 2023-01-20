#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        n = len(nums)
        for num in nums:
            presum.append(num + presum[-1])

        cnt = 0
        map = {}
        map[0] = 1  # 注意此行
        for i in range(1, n + 1):
            target = presum[i] - k
            cnt += map.get(target, 0)
            if presum[i] in map.keys():
                map[presum[i]] += 1
            else:
                map[presum[i]] = 1

        return cnt


# @lc code=end
