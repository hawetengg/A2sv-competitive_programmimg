class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prev = {}
        best = 10 ** 12

        current = 0
        prev[0] = -1

        for index, x in enumerate(nums):
            current += x
            current %= p

            if (current - target) % p in prev:
                best = min(index - prev[(current - target) % p], best)
            prev[current] = index
        if best >= len(nums):
            return -1
        return best