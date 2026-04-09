class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = []
        for i in range(len(nums)):
            n = 1
            while ((nums[i] + n) in nums):
                n +=1 
            else :
                result.append(n)
                n = 1
        result.sort()
        if len(nums) == 0:
            return 0 
        else:
         return result[-1]