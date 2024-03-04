class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            permutiations = self.permute(nums)

            for val in permutiations:
                val.append(n)

            ans.extend(permutiations)
            nums.append(n)

        return ans

        