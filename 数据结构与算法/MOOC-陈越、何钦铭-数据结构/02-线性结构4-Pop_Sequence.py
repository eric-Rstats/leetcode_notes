# Given a stack which can keep M numbers at most. Push N numbers in the order of 1, 2, 3, ..., N and pop randomly. You are supposed to tell if a given sequence of numbers is a possible pop sequence of the stack. For example, if M is 5 and N is 7, we can obtain 1, 2, 3, 4, 5, 6, 7 from the stack, but not 3, 2, 1, 7, 5, 6, 4.

# Input Specification:
# Each input file contains one test case. For each case, the first line contains 3 numbers(all no more than 1000): M(the maximum capacity of the stack), N(the length of push sequence), and K(the number of pop sequences to be checked). Then K lines follow, each contains a pop sequence of N numbers. All the numbers in a line are separated by a space.

# Output Specification:
# For each pop sequence, print in one line "YES" if it is indeed a possible pop sequence of the stack, or "NO" if not.

# Sample Input:
# 5 7 5
# 1 2 3 4 5 6 7
# 3 2 1 7 5 6 4
# 7 6 5 4 3 2 1
# 5 6 4 3 7 2 1
# 1 7 6 5 4 3 2

# Sample Output:
# YES
# NO
# NO
# YES
# NO


class Stack:

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        return self.items.pop()

    def push(self, x):
        self.items.append(x)

    def peak(self):
        """栈顶元素
        """
        return self.items[len(self.items)-1]


def vertify(sequence, M, N):
    """判定某一个输入是否是可能的序列

    Parameters
    ----------
     sequence : 序列.
     M : 栈的最大深度.
     N: 1-N 的序列长度.


    Returns
    -------
     flag: yes or no
    """

    l = [int(i) for i in sequence.split()]

    s1 = Stack()  # 初始化一个空栈
    s2 = Stack()  # 初始化一个空栈,作为出栈的模拟

    # 将序列的元素反向一个个压入s1
    for i in range(len(l)):
        s1.push(l[len(l)-i-1])

    i = 0
    while i <= N:

        if not s2.is_empty() and s1.peak() == s2.peak():
            # 当栈顶元素相同时，且s2不是空栈时，pop
            s1.pop()
            s2.pop()

        elif len(s2) < M and i < N:
            s2.push(i+1)
            i += 1
        else:
            break

    if s1.is_empty() and s2.is_empty():
        return "YES"
    else:
        return "NO"


m, n, k = [int(i) for i in input().split()]

tmp = dict()
for i in range(k):
    tmp[i] = input()

for i in range(k):
    print(vertify(tmp[i], m, n))
