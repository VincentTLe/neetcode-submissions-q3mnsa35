class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        compare={}
        for char in s : 
            if char not in compare:
                compare[char] = 1
            else :
                compare[char] +=1 
        for char in t :
            if char not in compare or compare[char] == 0:
                return False 
            else:
                compare[char] -= 1 
        return True
    