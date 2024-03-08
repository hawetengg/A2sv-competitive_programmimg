class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        count = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + 2 ** (right - left)) % mod
                left += 1
            else:
                right -= 1
                
        return count

        