#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 定义出现的字符集合
        char_set = {}
        max_size = 0
        start = 0
        for i in range(len(s)):
            if s[i] in char_set:
                start = max(char_set[s[i]], start)
            max_size = max(max_size, i-start+1)
            char_set[s[i]] = i+1

        return max_size

        # @lc code=end
