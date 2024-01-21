class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total = 0
        num_set = set()
        l = 0
        max_score = 0

        for r in range(len(nums)):
            while nums[r] in num_set:
                total -= nums[l]
                num_set.remove(nums[l])
                l += 1
            num_set.add(nums[r])
            total += nums[r]
            max_score = max(max_score, total)
        return max_score
                
