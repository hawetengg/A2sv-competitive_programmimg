class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        look_up = {0 : 1}

        for i in range(len(nums)):
            total += nums[i]
            diff = total - k
            if diff in look_up:
                res += look_up[diff]
            look_up[total] = look_up.get(total, 0) + 1
        return res