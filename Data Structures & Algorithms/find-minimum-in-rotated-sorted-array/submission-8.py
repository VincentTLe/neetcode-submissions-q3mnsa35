class Solution:
    def findMin(self, nums: List[int]) -> int:
        #f<m<l: return f
        # if m>f and m>l: m+=1
        #if m<f and m<l: mm-=1
        
        first = 0
        last = len(nums)-1
        res = 1000000
    
        while first <= last:
            f = nums[first]
            l = nums[last]
            mid = first + (last-first)//2
            m = nums[mid]
            if f<=m<=l: 
                res = min(res,f)
                break
            elif m>=f:
                res = min(res,f)
                first = mid+1
            else:
                res = min(res,m)
                last = mid-1 

        return res

