from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # Sort the string to create a unique key
            sorted_s = "".join(sorted(s))
            # Append the original word to that key's list
            res[sorted_s].append(s)

        # Return all grouped sublists
        return list(res.values())