class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = len(set(nums))
        count = 0

        for i in range(len(nums)):
            sett = set()
            for j in range(i, len(nums)):
                sett.add(nums[j])
                if len(sett) == s:
                    count += 1
                elif len(sett) > s:
                    break
        return count
        