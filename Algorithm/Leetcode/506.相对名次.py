#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc = ("Gold Medal", "Silver Medal", "Bronze Medal")
        arr = sorted(enumerate(score), key=lambda x: -x[1])
        ans = [""] * len(score)
        for i, (idx, _) in enumerate(arr):
            ans[idx] = desc[i] if i < 3 else str(i + 1)
        return ans


# @lc code=end
