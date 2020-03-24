#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.58%)
# Likes:    384
# Dislikes: 0
# Total Accepted:    29.7K
# Total Submissions: 83.6K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
#
# 说明：
#
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, start = 0, 0, 0
        minLen = float('inf')
        needs = dict(Counter(t))
        window = {item: 0 for item in needs}
        match = 0

        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    # 如果出现次数对上了
                    match += 1
            #right += 1

            while match == len(needs):
                # 如果都找到了，需要把left移动了
                if minLen > right - left + 1:
                    start = left
                    minLen = right - left + 1
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1

            right += 1
        return "" if minLen == float('inf') else s[start:start+minLen]


# @lc code=end
