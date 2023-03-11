#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (41.86%)
# Likes:    235
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 47.8K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
#
# 示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
# 示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#
#

# @lc code=start

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        result = []
        hashmap1 = {}
        hashmap2 = Counter(p)
        for right in range(len(s)):
            tail = s[right]
            hashmap1[tail] = hashmap1.get(tail, 0) + 1

            if hashmap1 == hashmap2:
                result.append(left)
            if right - left + 1 >= len(p):
            # if right >= len(p) - 1:
                head = s[left]
                hashmap1[head] -= 1
                if hashmap1[head] == 0:
                    del hashmap1[head]
                left += 1
        return result


        # left, right, start = 0, 0, 0
        # needs = dict(Counter(p))
        # window = {item: 0 for item in needs}
        # match = 0
        # result = []

        # while right < len(s):
        #     c1 = s[right]
        #     if c1 in needs:
        #         window[c1] += 1
        #         if window[c1] == needs[c1]:
        #             # 如果出现次数对上了
        #             match += 1
        #     #right += 1

        #     while match == len(needs):
        #         # 如果都找到了，需要把left移动了
        #         if len(p) == right - left + 1:
        #             result.append(left)
        #         c2 = s[left]
        #         if c2 in needs:
        #             window[c2] -= 1
        #             if window[c2] < needs[c2]:
        #                 match -= 1
        #         left += 1

        #     right += 1
        # return result


# @lc code=end
