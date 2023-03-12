class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        left, right = 0, 0
        hashmap = {}
        cum_sum = [0]
        # 前缀和
        for item in array:
            if item.isdigit():
                cum_sum.append(cum_sum[-1] + 1)
            else:
                cum_sum.append(cum_sum[-1] - 1)
        
        # 寻找前缀和相同的最长窗口大小
        for i, v in enumerate(cum_sum):
            j = hashmap.get(v, -1)
            if j < 0:
                # 首次发现
                hashmap[v] = i
            elif i - j > right - left:
                right, left = i, j
        return array[left:right]