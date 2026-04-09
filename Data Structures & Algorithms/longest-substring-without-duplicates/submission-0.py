class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        longest = 0 
        for R, ch in enumerate(s):
            while ch in window:
                window.remove(s[L])
                L+=1
            window.add(ch)
            longest = max(longest, R-L+1)
        return longest
        # s = "abba" -> L = 0 -> s[L]= a, 