class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        # 
        while i < len(nums)-2:
            if i>0 and nums[i] == nums[i - 1]:
                i+=1 
                continue
            j = i+1 
            k = len(nums) - 1
            target = -nums[i]
            while (j<k):
                s = nums[j] + nums[k]
                if (s == target):
                    result.append([nums[i],nums[j],nums[k]])    

                    #skip duplicate in the left
                    val_j = nums[j]
                    while j<k and nums[j] == val_j:
                        j+=1
                    #skip duplicate in the right 
                    val_k = nums[k]
                    while j<k and nums[k] == val_k:
                        k-=1
                elif (s < target):
                    j+=1
                else:
                    k-=1
            i+=1
        return result