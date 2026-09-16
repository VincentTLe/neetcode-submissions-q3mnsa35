class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):

            for s in strs:
                # Case 1 : length of string is equal to i which mean the string is shorter than the first str , then just end it there
                # Case 2 :  the character at index i is different 
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]