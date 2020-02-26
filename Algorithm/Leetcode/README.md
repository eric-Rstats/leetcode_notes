[toc]


# leetcode

## 3.最长非重复子串长度

利用hashmap，比如字典存储某个字符的位置，当指针所指向的字符已经出现过之后，将start移到前一次出现之后，计算最大长度并更新。

    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            # 定义出现的字符集合
            char_set = {}
            max_size = 0
            start = 0
            for i in range(len(s)):
                if s[i] in char_set:
                    start = max(char_set[s[i]], start)
                max_size = max(max_size, i-start+1)
                char_set[s[i]] = i+1
    
            return max_size
    

## 4.寻找两个有序数组的中位数

给定两个有序数组分别长度为m和n，输出两个数组的中位数

## 5.最长回文子串

从字符串的某一个位置向左右去传播。可能会产生奇数长度的字符串，也可能会产生偶数长度的字符串。

+ 复杂度是O(n^2)

    class Solution:
        def longestPalindrome(self, s: str) -> str:
            size = len(s)
            if size < 2:
                return s
    
            # 至少长度是1
            max_len = 1
            res = s[0]
    
            for i in range(len(s)):
                # 奇数串,从当前索引向两边去传播
                s_odd, len_odd = self.spread(s, i, i)
                # 偶数串
                s_even, len_even = self.spread(s, i, i + 1)
    
                s_longest = s_odd if len_odd >= len_even else s_even
    
                if len(s_longest) > max_len:
                    max_len = len(s_longest)
                    res = s_longest
            return res
    
        def spread(self, s, i, j):
            """中心传播
            Paramter:
            s: 字符串
            i: 左索引位置
            j: 右索引位置
            Returns:
            sub_string:子字符串
            len:子字符串的长度
            """
            # 计算字符串的长度
            size = len(s)
            while i >= 0 and j < size and s[i] == s[j]:
                i -= 1
                j += 1
    
            return s[i+1:j], j-i-1



## 141.判断链表是否有环

+ 利用快慢指针，如果快指针一次移动两个位置，慢指针一次移动一个位置。则若有环，快指针已经重新回到链表内部，则快指针会追上慢指针
+ 利用哈希，将每次出现的存下来，如果出现了重复，则说明有环

    class Solution:
        def hasCycle(self, head: ListNode) -> bool:
            # # 1.快慢指针法
            # if head is None or head.next is None:
            #     return False
            # # 快慢指针
            # fast = head.next
            # slow = head
            # while (slow != fast):
            #     if fast is None or fast.next is None:
            #         return False
            #     else:
            #         slow = slow.next
            #         fast = fast.next.next
    
            # return True
    
            # 2. hash
            dict = {}
            current = head
            while current is not None:
                if current not in dict:
                    dict[current] = 1
                    current = current.next
                else:
                    return True
            return False


## 14.最长公共前缀

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 当前最长公共前缀长度

        len_str = [len(s) for s in strs]
        min_len = 0 if len(len_str) == 0 else min(len_str)
        cnt_str = len(strs)  # 字符串数组的长度
        if min_len == 0:
            return ""
        for i in range(min_len):
            tmp = strs[0][i]
            for j in range(1, cnt_str, 1):
                if strs[j][i] != tmp:
                    return strs[0][:i]
        return strs[0][:i+1]

```

## 26. 删除排序数组中的重复项

+ 利用双指针：
当左指针与右指针的值相同时，右指针继续往后寻找不同值；
当发现不同值后，复制到left+1位置，left此刻移动到left+1位置。
while的终止条件是右指针到最边界。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left+1

```
