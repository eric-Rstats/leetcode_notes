[toc]

# LeetCode

Fucking-Alogorithm学习笔记: https://labuladong.gitbook.io/algo/

## 1. 动态规划

## 2. 回溯算法

## 3. 二分查找

### 3.1 基础框架

```python
def BinarySearch(nums, target):
  left = 0
  right = ……
  
  while(……):
    mid = left + (right - left)/2
    if nums[mid] == target:
      ……
    elif nums[mid] < target:
      left = ……
    elif nums[mid] > target:
      right = ……
  
  return ……
```

如上`……`表示可能出现细节问题的地方。使用`left+(right-left)/2`是为了防止`left`和`right`太大直接相加导致溢出。

+ `while`的区间怎么写: `left  <= right`则是左闭右闭
+ 终止条件：找到的话，就返回。如果整个循环终止，还没有找到，就`return` -1
+ `left`和`right`更新：左闭右闭的话，就是`left=mid+1,right=mid-1`

### 3.2 算法缺陷

假如给定数组`nums=[1,2,2,2,3]`，`target=2`则此算法返回的索引是2，但如果想要返回左侧边界或者右侧边界都无法处理。

### 3.3 寻找左侧边界

```python
def BinarySearch(nums, target):
  left = 0
  right = len(nums)-1
  
  while(left <= right):
    mid = left + (right - left)/2
    if nums[mid] == target:
      right = mid - 1
    elif nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
  # 考虑边界问题
  if (left >= len(nums) or nums[left] != target):
    return -1
  return left
```

### 3.4 寻找右侧边界

```python
def BinarySearch(nums, target):
  left = 0
  right = len(nums)-1
  
  while(left <= right):
    mid = left + (right - left)/2
    if nums[mid] == target:
      left = mid + 1
    elif nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
  # 考虑边界问题
  if (right <= 0 or nums[right] != target):
    return -1
  return right
```

如上所述，边界问题都是target比nums的数都大，或者都小的情况。

### 3.5 相关题目

|                             题目                             |                      是否解决                      | 难度 |
| :----------------------------------------------------------: | :------------------------------------------------: | :--: |
| [704.二分查找](https://leetcode-cn.com/problems/binary-search/) | [704.二分查找_solved_](./Leetcode/704.二分查找.py) | Easy |



## 4. 滑动窗口解题套路框架



### 4.1 最小覆盖子串

[76.最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

> 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
>
> 示例：
>
> 输入: S = "ADOBECODEBANC", T = "ABC"
> 输出: "BANC"
> 说明：
>
> 如果 S 中不存这样的子串，则返回空字符串 ""。
> 如果 S 中存在这样的子串，我们保证它是唯一的答案。

```Python
# 从字符串S中寻找包含T中所有字母的最小子串
# 从S中设置left,right，比较窗口中是否出现。都出现后，再逐渐缩小left。当又出现对应不上的时候，再右移right

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, start = 0, 0, 0
        minLen = float('inf')
        needs = dict(Counter(t))
        window = {item: 0 for item in needs}
        match = 0

        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    # 如果出现次数对上了
                    match += 1
            #right += 1

            while match == len(needs):
                # 如果都找到了，需要把left移动了
                if minLen > right - left + 1:
                    start = left
                    minLen = right - left + 1
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1

            right += 1
        return "" if minLen == float('inf') else s[start:start+minLen]
```

### 4.2 找到字符串中所有字母异位词

[438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

> 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
>
> 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
>
> 说明：
>
> 字母异位词指字母相同，但排列不同的字符串。
> 不考虑答案输出的顺序。
> 示例 1:
>
> 输入:
> s: "cbaebabacd" p: "abc"
>
> 输出:
> [0, 6]
>
> 解释:
> 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
> 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
>  示例 2:
>
> 输入:
> s: "abab" p: "ab"
>
> 输出:
> [0, 1, 2]
>
> 解释:
> 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
> 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
> 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

```python
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, start = 0, 0, 0
        needs = dict(Counter(p))
        window = {item: 0 for item in needs}
        match = 0
        result = []

        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    # 如果出现次数对上了
                    match += 1
            #right += 1

            while match == len(needs):
                # 如果都找到了，需要把left移动了
                if len(p) == right - left + 1:
                    result.append(left)
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1

            right += 1
        return result
```

### 4.3 无重复的最长子串

[3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

> 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
>
> 示例 1:
>
> 输入: "abcabcbb"
> 输出: 3 
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
> 示例 2:
>
> 输入: "bbbbb"
> 输出: 1
> 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
> 示例 3:
>
> 输入: "pwwkew"
> 输出: 3
> 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
>      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        result = 0
        needs = dict(Counter(s))
        window = {item: 0 for item in needs}

        while right < len(s):
            c1 = s[right]
            window[c1] += 1

            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1

            result = max(result, right-left+1)

            right += 1
        return result
```

### 4.4 题目





## 5. 双指针

左右指针、快慢指针。前者主要解决链表中的问题，比如链表中是否有环；后者主要解决数组（字符串）的问题，比如二分查找。

### 5.1 快慢指针

#### 判断链表中是否有环

利用快慢指针，如果有环，则快指针和慢指针必定会遭遇

[141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (fast == slow):
                return True

        return False
```

#### 已知链表中有环，返回这个环的起始位置

[142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

只需要在相遇后，额昂快慢指针中的任一个指向head，然后同速前进，再相遇的时候就是环的起点。

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while True:
            # 为了当没有环的时候跳出
            if not (fast and fast.next):
                return
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
```

#### 寻找链表的中点

[878.链表的中间结点](https://leetcode-cn.com/problems/middle-of-the-linked-list/)

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

####  寻找链表的倒数第k个元素

[19. 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

先让快指针移动k步，之后两个指针一起，当快指针指向末尾的时候，慢指针恰好是倒数第k个链表节点。

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
```

### 5.2 左右指针

#### 二分查找

```python
def binarySearch(nums, target):
  left = 0
  right = len(nums) - 1
  
  while left <= right:
    mid = left + (right-left) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      right = mid - 1
    elif nums[mid] < target:
      left = mid + 1
      
   return -1
```

#### 两数之和

[167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return -1
```

#### 反转数组

```python
def reverse(nums):
  left = 0
  right = len(nums) - 1
  while left < right:
    nums[left], nums[right] = nums[right],nums[left]
    left += 1
    right -= 1
```

