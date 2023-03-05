#
# @lc app=leetcode.cn id=2363 lang=python3
#
# [2363] 合并相似的物品
#

# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = Counter()
        for value, weight in items1:
            dic[value] += weight
        for value, weight in items2:
            dic[value] += weight

        res = sorted([a, b] for a, b in dic.items())

        return res

# @lc code=end
