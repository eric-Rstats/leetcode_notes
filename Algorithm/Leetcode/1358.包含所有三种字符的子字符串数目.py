#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#
# https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (52.68%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 19.8K
# Testcase Example:  '"abcabc"'
#
# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
# 
# 请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
# 
# 
# 示例 2：
# 
# 输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
# 
# 
# 示例 3：
# 
# 输入：s = "abc"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= s.length <= 5 x 10^4
# s 只包含字符 a，b 和 c 。
# 
# 
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashmap = {}
        left, cnt = 0, 0
        for right in range(len(s)):
            tail = s[right]
            hashmap[tail] = hashmap.get(tail, 0) + 1
            # if min(items) == 1 and max(items) == 1:
            #     cnt += 1
            while len(hashmap) == 3:
                cnt += len(s) - right # 以left,right为开头的所有子串都满足
                head = s[left]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                left += 1


        return cnt

# @lc code=end

