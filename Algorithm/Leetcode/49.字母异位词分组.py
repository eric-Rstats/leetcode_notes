#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 版本1: 字典序排序后使用哈希表
        # charmap={}

        # for i in range(len(strs)):
        #     s = strs[i]
        #     key = "".join(sorted(s))
        #     if key in charmap:
        #         charmap[key].append(s)
        #     else:
        #         charmap[key] = [s]

        # return list(charmap.values())

        # 版本2: 统计字母出现次数
        char_map = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord("a")] += 1
            char_map[tuple(cnt)].append(s)

        return list(char_map.values())


# @lc code=end
