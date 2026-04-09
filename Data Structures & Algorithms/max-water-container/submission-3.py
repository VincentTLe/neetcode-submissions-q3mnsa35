class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = (j-i) * min(heights[i], heights[j])
        while (i < j):
            if (heights[i] < heights[j]):
                i+=1
                area = max((j-i) * min(heights[i], heights[j]), area)
            else:
                j-=1
                area = max((j-i) * min(heights[i], heights[j]), area)
        return area