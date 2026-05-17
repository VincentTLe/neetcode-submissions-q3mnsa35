class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = len(set(nums))
        if s != len(nums):
            return True 
        else:
            return False
