#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = []
        for i, temp in enumerate(temperatures):
            # temp = temperatures[i]
            if not stack or temperatures[stack[-1]] >= temp:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    pre = stack.pop()
                    res[pre] = i - pre
                stack.append(i)
        return res
# @lc code=end
