#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode.cn/problems/palindromic-substrings/description/
#
# algorithms
# Medium (66.88%)
# Likes:    1134
# Dislikes: 0
# Total Accepted:    267K
# Total Submissions: 399.5K
# Testcase Example:  '"abc"'
#
# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# 
# 回文字符串 是正着读和倒过来读一样的字符串。
# 
# 子字符串 是字符串中的由连续字符组成的一个序列。
# 
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        res += 1
                        dp[i][j] =True
                    elif dp[i+1][j-1]:
                        res += 1
                        dp[i][j] =True
        return res
    #     result = 0
    #     for i in range(len(s)):
    #         result += self.extend(i, i, s)
    #         result += self.extend(i, i+1, s)
    #     return result

    #  # 中心扩散法
    # def extend(self, left, right, s):
    #     n = len(s)
    #     cnt = 0
    #     while left >= 0 and right < n and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #         cnt += 1
    #     return cnt
# @lc code=end

