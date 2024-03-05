class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        candidates.sort()

        def backtrack(start):
            if sum(arr) == target:
                ans.append(arr[:])
                return 

            elif sum(arr) > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(i + 1)
                arr.pop()
        
        backtrack(0)
        return ans
        