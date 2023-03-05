#
# @lc app=leetcode.cn id=2570 lang=python3
#
# [2570] 合并两个二维数组 - 求和法
#

# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = Counter()
        for k, v in nums1:
            dic[k] = v
        for k, v in nums2:
            dic[k] += v

        return sorted([k, v] for k, v in dic.items())
# @lc code=end
