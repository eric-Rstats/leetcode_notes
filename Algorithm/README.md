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

