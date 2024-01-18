class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                k -= 1
                count = 0
            while k == 0:
                if nums[l] % 2 != 0:
                    k += 1
                count += 1
                l += 1
            ans += count
        return ans

        