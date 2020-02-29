# -*- coding:utf-8 -*-
# 思路1：修改数组


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


# 思路2：哈希表，内存消耗大一些
class Solution2:
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

# 思路3：二分查找，不进行数组的修改（不通用，有些边界情况不行）


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums is None or nums == 0:
            return False
        start = 0
        end = len(nums) - 1

        while end >= start:
            middle = (end+start) // 2
            cnt = self.countRange(nums, start, middle)
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
