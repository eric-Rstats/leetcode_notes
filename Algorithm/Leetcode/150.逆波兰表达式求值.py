#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t not in operations:
                stack.append(t)
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(eval(f"{v2} {t} {v1}")))
        return int(stack[-1])
# @lc code=end
