#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 定义出现的字符集合
#         char_set = {}
#         max_size = 0
#         start = 0
#         for i, item in enumerate(s):
#             if item in char_set:
#                 start = max(char_set[item], start)
#             max_size = max(max_size, i-start+1)
#             char_set[item] = i+1

#         return max_size

# @lc code=en


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        char_map = {}
        for right in range(len(s)):
            while s[right] in char_map:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
            char_map[s[right]] = 1

            result = max(result, right-left+1)
        return result
