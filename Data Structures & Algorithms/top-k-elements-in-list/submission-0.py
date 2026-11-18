class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        top_k_vals = sorted(list(counter.values()), reverse=True)[:k]
        top_k_keys = [num for num, count in counter.items() if count in top_k_vals]
        return top_k_keys
        