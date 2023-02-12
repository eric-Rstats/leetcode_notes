#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_absent = cnt_late = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == "A":
                cnt_absent += 1
            if cnt_absent >= 2:
                return False

            if ch == "L":
                cnt_late += 1
                if cnt_late >= 3:
                    return False
            else:
                cnt_late = 0

        return True


# @lc code=end
