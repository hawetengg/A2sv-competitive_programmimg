class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        zeros = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
                if zeros > 1:
                    while nums[l] == 1:
                        l += 1
                    zeros -= 1
                    l += 1
            count = max(count, r - l)        
        return count

        