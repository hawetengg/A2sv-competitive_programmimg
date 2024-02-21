class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = nums[0]

        for i in range(1, len(nums)):
            if i <= maxx:
                maxx = max(maxx, nums[i] + i)
            else:
                return False
        return True
            
