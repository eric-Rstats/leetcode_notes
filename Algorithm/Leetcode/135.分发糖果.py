#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # n = len(ratings)
        # res = [1 for _ in range(n)]
        # for i in range(1, n):
        #     if ratings[i] > ratings[i-1]:
        #         res[i] = res[i-1] + 1
        # for j in range(n-2, -1, -1):
        #     if ratings[j] > ratings[j+1]:
        #         res[j] = max(res[j], res[j+1]+1)
        # return sum(res)
        # 版本2
        # n = len(ratings)
        # left = [1 for _ in range(n)]
        # right = [1 for _ in range(n)]
        # for i in range(1, n):
        #     if ratings[i] > ratings[i-1]:
        #         left[i] = left[i-1] + 1
        # total = left[-1]
        # for j in range(n-2, -1, -1):
        #     if ratings[j] > ratings[j+1]:
        #         right[j] = right[j+1] + 1
        #     total += max(left[j], right[j])
        # return total
        # 版本3
        res = 1
        n = len(ratings)
        pre, inc, dec = 1, 1, 0

        for i in range(1, n):
            # 递增序列
            if ratings[i] >= ratings[i-1]:
                dec = 0 # 及时的更正为0
                pre = 1 if ratings[i] == ratings[i-1] else pre + 1 # 为什么我和你成绩一样，我只能吃一个?
                res += pre
                inc = pre
            # 递减序列
            else:
                dec += 1
                if dec == inc:
                    # 如果递减序列和递增序列长度相同了,那上一个递增序列末尾的值需要+1
                    dec += 1
                res += dec
                pre = 1 # 递减序列的末尾数，永远给1，这个值也只有下一个递增序列会使用
        return res


        
# @lc code=end
