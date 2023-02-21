#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        res1 = res2 = 0
        # guess = list(guess)
        # n = len(secret)
        # char_map = dict(Counter(secret))
        # for i in range(n):
        #     item = guess[i]
        #     if secret[i] == item:
        #         res1 += 1
        #         char_map[item] -= 1
        #         guess[i] = -1

        # for i in range(n):
        #     value = guess[i]
        #     if value != -1 and char_map.get(value, 0) != 0:
        #         res2 += 1
        #         char_map[value] -= 1
        s, g = [0] * 10, [0] * 10
        for i, j in zip(secret, guess):
            if i == j:
                res1 += 1
            else:
                s[int(i)] += 1
                g[int(j)] += 1
        res2 = sum(min(k, v) for k, v in zip(s, g))

        return "{}A{}B".format(res1, res2)


# @lc code=end
