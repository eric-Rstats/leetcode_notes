# 获取
size = int(input())
sequence = [int(x) for x in input().split()]

sum_max = -1
tmp = 0
first, last, tmp_first = 0,0,0


for i in range(size):
    tmp += sequence[i]
    if tmp > sum_max:   # 如果下一轮计算有提升，那么就将尾指针指向这里。头指针指向当前计算的开端
        sum_max = tmp
        last = i
        first = tmp_first
        
    elif tmp < 0:
        tmp = 0
        tmp_first = i+1  # 当前计算的开端

    
if  sum_max>= 0:
    # 如果和为0，那么说明最起码有一个元素为0，那么久返回它
    print(str(sum_max) + ' ' + str(sequence[first]) + ' ' + str(sequence[last]))
else:
    # 如果全部都是负数，直接返回0，不拿-1作为返回值
    print(str(0) + ' ' + str(sequence[0]) + ' ' + str(sequence[size-1]))
