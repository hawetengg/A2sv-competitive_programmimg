class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        left = 0 
        right = len(nums) - 1
        mid = right - 1
        while right > 1:
            while mid > left:
                if nums[left] + nums[mid] > nums[right]:
                    ans += (mid - left)
                    mid -= 1
                else:
                    left += 1
            left = 0
            right -= 1
            mid = right - 1
        return ans


        
                                              