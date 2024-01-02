class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]
        if int("".join(str(i) for i in nums)) == 0:
            return "0"
        else:
            return "".join(str(i) for i in nums)
        
        
