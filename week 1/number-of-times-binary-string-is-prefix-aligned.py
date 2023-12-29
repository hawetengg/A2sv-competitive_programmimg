class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        curr_sum = 0
        new_sum = 0
        for i, bulb in enumerate(light):
            new_sum += i + 1
            curr_sum += bulb
            if curr_sum == new_sum:
                res += 1
        return res