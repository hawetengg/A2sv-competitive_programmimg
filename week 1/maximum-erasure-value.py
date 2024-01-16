class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        seen = set()
        curr = 0
        l = 0
        r = 0
        while r < len(nums):
            while nums[r] in seen:
                curr -= nums[l]
                seen.remove(nums[l])
                l += 1
            curr += nums[r]
            res = max(res, curr)
            seen.add(nums[r])
            r += 1
        return res
                
