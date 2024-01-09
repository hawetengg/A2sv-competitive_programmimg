class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0

        for i in range(k):
            summ += nums[i]
        maxSum = summ
        i = 0
        j = k

        while j < len(nums):
            summ -= nums[i]
            i += 1
            summ += nums[j]
            j += 1
            maxSum = max(summ, maxSum)
        return maxSum/k

        