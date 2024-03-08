from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        look_up = defaultdict(list)
        res = [0] * len(nums)

        for i, x in enumerate(nums):
            look_up[x].append(i)
        
        def solve(x):
            arr = look_up[x]
            summ = 0
            
            for i in range(1, len(arr)):
                summ += arr[i] - arr[0]
            res[arr[0]] = summ

            for i in range(1, len(arr)):
                summ += (arr[i] - arr[i - 1]) * (i + 1)
                summ -= (arr[i] - arr[i - 1]) * (len(arr) - (i - 2) - 1)
                res[arr[i]] = summ
        
        for x in look_up.keys():
            solve(x)
        
        return res


