class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
         left = 0
         right = sum(nums)
         div_sum = [left + right]
         for i in range(len(nums)):
             if nums[i] == 0:
                 left += 1
             if nums[i] == 1:  
                right -= 1
             div_sum.append(left + right) 
         maxx = max(div_sum)
         return ([i for i, v in enumerate(div_sum) if v == maxx])


        