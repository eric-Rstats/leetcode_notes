#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]  # 前后各加1个0,防止纯递增递减
        res = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                right = i

                x = right - left - 1  # 宽
                y = heights[mid]  # 高
                res = max(res, x * y)
            stack.append(i)

        return res

# @lc code=end
