class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Understand :
        # Input : integers array of temperatures where temperatures[i] is daily temperature of ith day
        # output : result array where result[i] is the number of days after the ith day before a warmer temperature will appear for the ith day
        # plan : 
        # Use a for loop going all over the array, for each element, use a while loop until it reach an element that higher than the 
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i 
            stack.append(i)
        return result
            