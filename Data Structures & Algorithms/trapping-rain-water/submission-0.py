class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        prefix = suffix = 0 
        volume = 0 

        while left < right :
            if height[left] <= height[right]:
                if height[left] >= prefix:
                    prefix = height[left]
                else:
                    volume += prefix - height[left]
                left +=1 
            else :
                if height[right] >= suffix:
                    suffix = height[right]
                else:
                    volume += suffix - height[right]
                right -=1
        return volume
