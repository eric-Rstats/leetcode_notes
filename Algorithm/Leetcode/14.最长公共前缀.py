#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.40%)
# Likes:    892
# Dislikes: 0
# Total Accepted:    192.1K
# Total Submissions: 529.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 当前最长公共前缀长度

        # len_str = [len(s) for s in strs]
        # min_len = 0 if len(len_str) == 0 else min(len_str)
        # cnt_str = len(strs)  # 字符串数组的长度
        # if min_len == 0:
        #     return ""
        # for i in range(min_len):
        #     tmp = strs[0][i]
        #     for j in range(1, cnt_str, 1):
        #         if strs[j][i] != tmp:
        #             return strs[0][:i]
        # return strs[0][:i+1]
        # 版本1
        cnt_str = len(strs)
        len_str = [len(s) for s in strs]
        min_len = 0 if cnt_str == 0 else min(len_str)
        for i in range(min_len):
            for j in range(1, cnt_str):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_len]

        # 版本2:字典序排序(有不同的肯定会排在最小或者最大)
        if not strs:
            return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0
        # @lc code=end
