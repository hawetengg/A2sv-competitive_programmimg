class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        arr = []
        nums = []

        for i in range(1, 10):
            nums.append(i)

        def backtrack(start):
            if len(arr) == k and sum(arr) == n:
                ans.append(arr[:])
                return
            
            elif len(arr) > k or sum(arr) > n:
                return

            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1)
                arr.pop()

        backtrack(0)
        return ans
        