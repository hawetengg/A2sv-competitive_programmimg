class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
                while k < 0:
                    if nums[l] == 0:
                        k += 1
                    l += 1
            count = max(count, r - l + 1)
        return count
                
        
        
        