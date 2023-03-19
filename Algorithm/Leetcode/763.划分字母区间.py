#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0] * 26
        for i, ch in enumerate(s):
            hash[ord(ch)-ord('a')] = i
        left, right = 0, 0
        res = []
        for i, ch in enumerate(s):
            right = max(right, hash[ord(ch)-ord('a')])  # 每个字母的最大索引
            if right == i:
                l = right - left + 1
                res.append(l)
                left = i + 1
        return res
# @lc code=end
