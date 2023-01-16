#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        res = []
        start = -1
        for i, c in enumerate(s):
            if c == "(":
                start = i
            elif c == ")":
                res.append(d.get(s[(start + 1) : i], "?"))
                start = -1
            elif start < 0:
                res.append(c)

        return "".join(res)


# @lc code=end
