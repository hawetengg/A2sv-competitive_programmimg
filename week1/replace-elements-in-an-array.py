class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        lookup = {}
        for i, x in enumerate(nums):
            lookup[x] = i
        for j, k in operations:
            index = lookup[j]
            nums[index] = k
            lookup[k] = index
            del lookup[j]
        return nums
