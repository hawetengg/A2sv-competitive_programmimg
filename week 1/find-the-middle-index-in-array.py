class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0

        for i in range(len(nums)):
            cur += nums[i]
            if cur - nums[i] == total - cur:
                return i
        return -1