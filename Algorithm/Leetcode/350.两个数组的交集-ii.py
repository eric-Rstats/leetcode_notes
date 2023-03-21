#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        nums1.sort()
        nums2.sort()
        res = []
        while idx1 < m and idx2 < n:
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                res.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        return res
# @lc code=end
