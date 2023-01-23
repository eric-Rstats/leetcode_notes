#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue
                if board[i][j] == "X":
                    cnt += 1
        return cnt


# @lc code=end
