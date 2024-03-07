class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_W = sum(weights)
        left = max(weights)
        right = total_W
        minWeight = right
        
        def check(mid):
            count = 1
            cur_total = 0
            for i in range(len(weights)):
                if cur_total + weights[i] > mid:
                    count += 1
                    cur_total = 0
                cur_total += weights[i]
            return count <= days

        while left <= right:
            mid = (left + right) // 2
            check(mid)
            if check(mid):
                minWeight = min(minWeight, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minWeight
        


        