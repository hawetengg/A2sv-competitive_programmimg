class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_num = pow(10, 5)+1
        minn = max_num
        l,r = 0,0

        total = 0
        while r < len(nums):
            total += nums[r]

            while total >= target:
                minn = min(minn, r-l+1)
                total -= nums[l]
                l += 1

            r += 1

        return minn if minn != max_num else 0