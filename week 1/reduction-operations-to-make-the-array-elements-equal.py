class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        count = 0
        curr_num = 0

        for i, v in enumerate(nums):
            if curr_num != v:
                curr_num = v
                count += i
        return count

            



        