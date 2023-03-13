#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, result = 0, 0
        cnt = {}
        for right in range(len(fruits)):
            tail = fruits[right]
            cnt[tail] = cnt.get(tail, 0) + 1
            while len(cnt) > 2:
                head = fruits[left]
                cnt[head] -= 1
                if cnt[head] == 0:
                    del cnt[head]
                left += 1
            result = max(right-left+1, result)
        return result
# @lc code=end

