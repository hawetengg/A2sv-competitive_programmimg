class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        arr = [0] * k

        for i in range(len(nums)):
            total += nums[i] % k
            arr[total % k] += 1
        ans = arr[0]

        for j in arr:
            ans += (j * (j - 1)) // 2
            
        return ans

        