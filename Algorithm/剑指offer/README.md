# 剑指offer

代码在力扣上进行编程练习

## 第二章 面试需要的基础知识

### 数组中重复的数字

#### 1.修改数组的方式

[力扣-面试题03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

> 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

+ 解决思路：
可以进行排序，同时可以用哈希表来解决，不过哈希表的空间复杂度是$O(n)$，考虑使用空间复杂度为$O(1)$的方法。

+ 解法：
从头到尾扫描这个数组中的每个数字，当出现改位置数字不相等的时候，假设当前索引为i，值为m，若$i \neq m$，则交换i和m。若二者相等，说明找到一个重复数字。这么交换下去，直到碰到重复数字，或者整个遍历结束。

+ 临界条件：
要检查一下数组是否是空，元素是否越界

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums is None or nums == []:
            return False
        # 需要满足没有异常值
        for k in range(len(nums)):
            if nums[k] < 0 or nums[k] > len(nums)-1:
                return False
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
        return False

```


#### 2. 不修改数组找出重复的数字

> 在一个长度为n+1的数组里的所有数字都在1~n之间，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的数组.例如，如果输入常伟为8的数组{2,3,5,4,3,2,6,7},那么对应的输出是重复的数字2或者3。

+ 二分查找的思路:
从1~n范围内不断进行二分，如果用前面一半`1~m`的数目超过了m,说明这一半里面有重复的数字；否则，另一半的区间里包含重复数字。
具体操作是统计这个数组里，这两个区间出现的个数，而不是先排序。

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums is None or nums == 0:
            return False
        start = 0
        end = len(nums) - 1

        while end >= start:
            middle = (end+start) // 2
            cnt = self.countRange(nums,start, middle)
            if end == start:
                if cnt > 1:
                    return end
                else:
                    break
            if cnt > (middle - start + 1):
                end = middle
            else:
                start = middle + 1

        return False


    
    def countRange(self, nums, start, end):
        """查找数组nums在start和end之间的个数"""
        if nums is None or nums == []:
            return 0
        
        cnt = sum([1 for i in nums if i <= end and i >= start])
        return cnt
```

这种方式不能保证找出所有重复的数字，必须每一个取值的数字都出现，不然二分查找统计的数字不对，比如[0,0,1,2]可以，[0,0,2,3]不能统计出。所以这个《剑指offer》的方法不通用。
思考：如果需要找出所有重复数字怎么办?

#### 3. 哈希表的形式

如果面试官要求$O(1)$时间复杂度，允许用内存换时间。

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = {}
        if nums is None or nums == []:
            return False
        if max(nums) > len(nums)-1 or min(nums) < 0:
            return False
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                return nums[i]
        return False
```

