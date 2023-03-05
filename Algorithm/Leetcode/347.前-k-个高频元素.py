#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

import heapq

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        pri_que = []

        for num, freq in dic.items():
            heapq.heappush(pri_que, (freq, num))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        # 最小堆
        res = []
        for i in range(k-1, -1, -1):
            res.append(heapq.heappop(pri_que)[1])

        return res
# @lc code=end
