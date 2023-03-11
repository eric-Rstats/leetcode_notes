# 示例 1：
# 输入：[1,0,1,0,1]
# 输出：1
# 解释： 
# 有三种可能的方法可以把所有的 1 组合在一起：
# [1,1,1,0,0]，交换 1 次；
# [0,1,1,1,0]，交换 2 次；
# [0,0,1,1,1]，交换 1 次。
# 所以最少的交换次数为 1。

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # 统计1的个数
        n = sum(data)
        zeros, ones, left = 0, 0, 0
        min_swap = inf 

        for right in range(len(data)):
            if data[right] == 0:
                zeros += 1
            if right - left + 1 == n:
                min_swap = min(min_swap, zeros)

            if right >= n - 1:
                if data[left] == 0:
                    zeros -= 1
                left += 1
        return 0 if min_swap == inf else min_swap
