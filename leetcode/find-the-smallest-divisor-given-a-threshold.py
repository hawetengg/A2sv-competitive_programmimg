import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def divide(mid):
            total = 0
            for num in nums:
                total += math.ceil((num / mid))
            return total

        while left <= right:
            mid = (left + right) // 2
            total = divide(mid)
            if total <= threshold:
                right = mid - 1
            else:
                left = mid + 1
                
        return left

        