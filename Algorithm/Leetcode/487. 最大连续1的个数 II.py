class Solution:
    def longestOnes(self, nums: List[int]) -> int:
        left, one, zero = 0, 0, 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            else:
                one += 1
            
            if zero <= 1:
                result = max(result, right-left+1)
            
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                else:
                    one -= 1
                left += 1

        return result

