class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []

        def backtracking(start):
            if sum(arr) == target:
                ans.append(arr[:])
                return

            elif sum(arr) > target:
                return
            
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                backtracking(i)
                arr.pop()

        backtracking(0)
        return ans
        