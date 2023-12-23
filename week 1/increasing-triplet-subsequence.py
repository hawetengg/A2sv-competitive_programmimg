class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
       minn = float('inf')
       min_next = float('inf')

       for i in nums:
            if i <= minn:
               minn = i
            elif i <= min_next:
                min_next = i
            else:
                return True
       return False 


        