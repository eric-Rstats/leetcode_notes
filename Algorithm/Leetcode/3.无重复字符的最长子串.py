#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


""" class Solution:
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

        return max_size """

# @lc code=en


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        result = 0
        needs = dict(Counter(s))
        window = {item: 0 for item in needs}

        while right < len(s):
            c1 = s[right]
            window[c1] += 1

            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1

            result = max(result, right-left+1)

            right += 1
        return result
