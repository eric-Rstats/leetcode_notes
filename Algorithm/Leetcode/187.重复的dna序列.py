#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        hashmap = {}
        result = []
        left = 0
        for right in range(10, n+1):
            cur = s[left:right]
            if right-left == 10:
                if hashmap.get(cur, 0) == 1:
                    result.append(cur)
                hashmap[cur] = hashmap.get(cur, 0) + 1
                left += 1
        return result

        # 1. 哈希表
        # n = len(s)
        # hashmap = {}
        # result = []
        # for i in range(0, n-9):
        #     sub_string = s[i:i+10]
        #     times = hashmap.get(sub_string, 0)
        #     if times == 1:
        #         result.append(sub_string)
        #     hashmap[sub_string] = times + 1
        # return result
        # @lc code=end
