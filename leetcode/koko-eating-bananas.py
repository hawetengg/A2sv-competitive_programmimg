import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minVal = float(inf)

        def add(mid):
            total = 0
            for b in piles:
                total += (math.ceil(b / mid))
            return total


        while left <= right:
            mid = (left + right) // 2
            total = add(mid)

            if total <= h:
                minVal = min(minVal, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minVal
                
            
        