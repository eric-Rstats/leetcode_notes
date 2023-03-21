#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # 栈里面存储index索引
        n = len(height)
        res = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                down = stack.pop()  # 凹槽
                if not stack:
                    break
                left = stack[-1]  # 左边的墙
                right = i  # 右边的墙

                # 宽度
                x = right - left - 1
                # 高度
                y = min(height[left], h) - height[down]  # 积水高度是矮墙-凹槽
                res += x * y

            stack.append(i)
        return res

# @lc code=end
