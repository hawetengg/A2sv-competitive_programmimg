class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_W = sum(weights)
        left = max(weights)
        right = total_W
        min_day = right
        
        def check(mid):
            count = 1
            cur_total = mid
            for i in range(len(weights)):
                if cur_total - weights[i] < 0:
                    count += 1
                    cur_total = mid
                cur_total -= weights[i]
            return count <= days

        while left <= right:
            mid = (left + right) // 2
            check(mid)
            if check(mid):
                min_day = min(min_day, mid)
                right = mid - 1
            else:
                left = mid + 1

        return min_day
        


        