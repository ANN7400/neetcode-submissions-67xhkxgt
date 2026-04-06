import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Binary search range for the eating rate k
        low = 1
        high = max(piles)
        
        while low < high:
            k = (low + high) // 2
            total_hours = 0
            
            for p in piles:
                # Calculate hours for current pile: ceil(p / k)
                total_hours += math.ceil(p / k)
            
            if total_hours <= h:
                # Rate is feasible, try to find a smaller one
                high = k
            else:
                # Rate is too slow, must increase k
                low = k + 1
                
        return low