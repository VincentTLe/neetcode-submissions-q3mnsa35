class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0 
        best = 0 
        freq = [0] * 26
        maxf = 0
        for R,ch in enumerate(s):
            i = ord(ch) - ord('A')
            freq[i] += 1
            maxf = max(maxf, freq[i]) # maximum frequency character 
        # number of replacement = len(s) - maxf 
        # while number of replacement > k -> increase the L 
            while ((R-L+1 - maxf) > k):
                freq[ord(s[L]) - ord('A')] -= 1
                L+=1 
        # s = "XYYXX" k = 2
        # [0, ... 3, 2, 0] -> 
        # [X,Y,Y,X,X]
        # if R = 4 -> R-L + 1 = 5 - maxf = 3 > k  = 2
        # [0, ... , 2,2,0]
        # L+=1 
            best = max(best, R-L+1)
        return best
