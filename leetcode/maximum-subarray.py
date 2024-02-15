class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxx = nums[0]

        for i in nums:
            if summ < 0:
                summ = 0
            summ += i
            maxx = max(maxx, summ)
        return maxx 

        