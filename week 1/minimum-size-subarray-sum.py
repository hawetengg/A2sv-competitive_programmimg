class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = float('inf')
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                count = min(count, r - l + 1)
                total -= nums[l]
                l += 1
        if count == float('inf'):
            return 0
        else:
            return count