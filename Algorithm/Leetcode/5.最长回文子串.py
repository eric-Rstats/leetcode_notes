#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.44%)
# Likes:    6251
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 3.6M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = self.extend(i, i, s)
            l2, r2 = self.extend(i, i+1, s)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end+1]
    
    def extend(self, left, right, s):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return left+1, right-1
# @lc code=end

