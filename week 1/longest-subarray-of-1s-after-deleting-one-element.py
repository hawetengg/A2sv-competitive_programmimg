class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        zeros = 1
        l, r = 0, 0

        while(l < len(nums) and r < len(nums)):
            if nums[r] == 0:
                zeros -= 1
                if zeros < 0:
                    while nums[l] == 1:
                        l += 1
                    zeros += 1
                    # r += 1
                    # count = max(count, r - l)
                    l += 1
           
            count = max(count, r - l)
            r += 1        
        return count

        """
        if nums[l] == 0:
                        zeros += 1
                    l += 1
        """


        