#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        items = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for k in s:
            if k in items:
                stack.append(items[k])
            elif not stack or stack[-1] != k:
                return False
            else:
                stack.pop()
        return True if not stack else False

# @lc code=end
