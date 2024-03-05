class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []
        nums.sort()

        def backtrack(i, subsets):
            if i == len(nums):
                ans.append(subsets[:])
                return ans
            
            subsets.append(nums[i])
            backtrack(i + 1, subsets)
            subsets.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subsets)

        backtrack(0, subsets)
        return ans

