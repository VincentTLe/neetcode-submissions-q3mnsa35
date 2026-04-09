class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First-step : Count frequency
        freq={}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        # Second-step : Sorted by decreasing order:
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse = True)

        # Third-step : Take out k number :
        top_k = [num for num, count in sorted_items[:k]]
        return top_k