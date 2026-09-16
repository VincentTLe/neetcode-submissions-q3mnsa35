class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            # Compare character 'i' across all strings in the array
            for s in strs:
                # Check if index 'i' is out of bounds or characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        
        # If no mismatch occurs, the full first string is the common prefix
        return strs[0]