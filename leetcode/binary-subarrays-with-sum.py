class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def subArr(nums, total):
            prefix = 0
            j = 0
            count = 0
            if total < 0:
                return 0
            for i in range(len(nums)):
                prefix += nums[i]
                while prefix > total:
                    prefix -= nums[j]
                    j += 1
                count += (i - j + 1)
            return count

        return subArr(nums, goal) - subArr(nums, goal - 1)
    
    