import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles.sort()
        max_k = max(piles)#piles[-1]
        low = 1
        high = max_k

        while low <= high:
            mid = low + (high - low) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/mid)
            if total_time <= h:
                max_k = min(max_k, mid)
                high = mid - 1
                
            elif total_time > h:
                low = mid + 1

        return max_k

        

        

            
        