head, N, K = [x for x in input().split()]
N = int(N)
K = int(K)

# 用字典存储 地址 -> 数值 的一一对应关系
itemlist = {}

# 存储地址
address = {}

# 存储数据
for i in range(N):
    tmp = input().split()
    itemlist[tmp[0]] = int(tmp[1])
    address[tmp[0]] = tmp[2]


# 为了避免无效结点，先计算实际有多少个
tmp = head
for n in range(1, N+1):
    tmp = address[tmp]
    if tmp == "-1":
        break

# 构造一个长度为K的栈，作为翻转的媒介

s, output = [], []  # 栈，结果

current = head  # 当前指针
i = 0

while n // K > 0:
    # 当还需要翻转时，继续进行翻转

    while i < K:
        # push入栈
        s.append(current)
        current = address[current]  # 获取下一个结点存储位置
        i += 1

    while i > 0:
        # pop 出栈
        pop_item = s.pop()
        output.append(pop_item)
        i -= 1

    n -= K

# 对于剩下的一些元素，不需要翻转(如果还有剩余的话)
while current != '-1':
    output.append(current)
    current = address[current]

output.append(-1)


# 输出
for i in range(len(output)-1):
    key = output[i]
    print(str(key) + ' ' + str(itemlist[key]) + ' ' + str(output[i+1]))
