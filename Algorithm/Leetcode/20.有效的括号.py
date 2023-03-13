#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()
        return True if not stack else False

# @lc code=end
