class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = []

        def backtracking(start, arr):
            if len(arr) == k:
                ans.append(arr.copy())
                return
            
            for i in range(start, n + 1):
                arr.append(i)
                backtracking(i + 1, arr)
                arr.pop()
                
        backtracking(1, arr)
        return ans
        
        