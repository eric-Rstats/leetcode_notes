class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, result = 0, 0
        char_map = {}
        for right in range(len(s)):
            tail = s[right]
            char_map[tail] = char_map.get(tail, 0) + 1

            if len(char_map) <= 2:
                result = max(right-left+1, result)
            
            while right-left+1 > 2:
                head = s[left]
                char_map[head] -= 1
                if char_map[head] == 0:
                    del char_map[head]
                left += 1
        return result
