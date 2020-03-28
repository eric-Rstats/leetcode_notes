#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# https://leetcode-cn.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (64.26%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 69.5K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用队列实现栈的下列操作：
#
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
#
#
# 注意:
#
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty
# 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
#
#
#

# @lc code=start
from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top_element = x

    def pop(self) -> int:
        while len(self.q1) > 1:
            t = self.q1.popleft()
            self.q2.appendleft(t)
            self.top_element = t
        tmp = self.q1.popleft()
        while self.q2:
            self.q1.appendleft(self.q2.popleft())
        return tmp

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
