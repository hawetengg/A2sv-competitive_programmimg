class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cA, cB, ans = 0, 0, 0
        arr = []
       

        for cA, cB in costs:
            arr.append([cB - cA, cA, cB])

        arr.sort()

        for i in range(len(arr)):
            if i < len(arr) // 2:
                ans += arr[i][2]
            else:
                ans += arr[i][1]

        return ans
            
        