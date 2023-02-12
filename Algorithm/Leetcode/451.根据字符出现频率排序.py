#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        # 版本1
        # char_map = {}
        # for ch in s:
        #     if ch in char_map:
        #         char_map[ch] += 1
        #     else:
        #         char_map[ch] = 1
        # items = sorted(char_map.items(), key=lambda x: x[1], reverse=True)
        # return "".join([k * v for k, v in items])

        char_map = {}
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1

        items = [(-val, key) for key, val in char_map.items()]
        heapq.heapify(items)
        res = ""
        while items:
            val, key = heapq.heappop(items)
            res += key * (-val)
        return res


# @lc code=end
