class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        total = sum(nums)
        leftSum = 0

        for i, n in enumerate(nums):
            rightSum = total - n - leftSum
            leftSize = i
            rightSize = len(nums) - i - 1

            ans.append(leftSize * n - leftSum + rightSum - rightSize * n)
            leftSum += n

        return ans

        