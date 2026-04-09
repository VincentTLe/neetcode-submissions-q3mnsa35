class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        # [ 100, 200, 1, 3, 4, 2] -> start number is 100 , 200 and 1 
        for i in s:
            if ( (i-1) not in s ):
                x = i 
                length = 1
                while x + 1 in s:
                    x +=1
                    length += 1 
                longest = max(longest, length)
        return longest