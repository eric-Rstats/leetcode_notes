# 获取序列长度和输入序列
size = input()
sequence = [int(x) for x in input().split()]

sum_max = sequence[0]
tmp = sequence[0]
for i in range(1,len(sequence)):
    tmp += sequence[i]
    if tmp > sum_max:
         sum_max = tmp
    elif tmp < 0:
        tmp = 0

print(sum_max)
