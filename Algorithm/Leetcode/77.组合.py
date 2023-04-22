#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (73.19%)
# Likes:    232
# Dislikes: 0
# Total Accepted:    39.4K
# Total Submissions: 53.9K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 组合其实就是限制了树深的DFS
        result, path = [], []

        def drawback(n, k, start):
            if k == len(path):
                result.append(path[:])
                return
            
            # 剪枝
            # n-start+1+len(path) = k 
            # 剩余的个数是否足够
            for i in range(start, n+2-(k-len(path))):
                path.append(i)
                drawback(n, k, i + 1)
                path.pop()

        drawback(n, k, 1)
        return result
# @lc code=end
