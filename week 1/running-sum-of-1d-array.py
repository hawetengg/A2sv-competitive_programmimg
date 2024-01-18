class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        summ = nums[0]

        for i in range(1, len(nums)):
            summ += nums[i]
            output.append(summ)
        return output