#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = ["1"]

        for i in range(1, n):
            value = i + 1
            t1 = 1 if value % 5 == 0 else 0
            t2 = 1 if value % 3 == 0 else 0

            if t1 == 1 and t2 == 1:
                s = "FizzBuzz"
            elif t2 == 1:
                s = "Fizz"
            elif t1 == 1:
                s = "Buzz"
            else:
                s = str(value)
            res.append(s)

        return res


# @lc code=end
