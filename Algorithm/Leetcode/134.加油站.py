#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # 版本1: 参考leetcode
        # slow, fast, total = 0, 0, 0
        # n = len(gas)
        # while slow < n:
        #     total += gas[fast % n] - cost[fast % n]
        #     fast += 1
        #     if total < 0:
        #         slow = fast
        #         total = 0
        #     elif fast - slow == n:
        #         return slow
        # return -1

        # 版本2:宫水三叶
        # 当位置i 作为「起点」验证失败后，验证过程中遍历过的位置就不需要再作为「起点」被验证了
        # n = len(gas)
        # start = 0
        # while start < n:
        #     if gas[start] < cost[start]:
        #         start += 1
        #         continue

        #     cur = gas[start] - cost[start]
        #     idx = start + 1
        #     while idx % n != start:
        #         cur += gas[idx % n] - cost[idx % n]
        #         # 没油了,说明不满足
        #         if cur < 0:
        #             break
        #         idx += 1
        #     if idx % n == start:
        #         return start
        #     # 否则从结尾处开始
        #     start = idx
        # return -1

        # 版本3: 代码随想录
        n = len(gas)

        start, cur, total = 0, 0, 0
        for i in range(n):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i+1
        if total < 0: return -1
        return start
        # @lc code=end
