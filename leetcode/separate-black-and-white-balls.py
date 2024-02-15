class Solution:
    def minimumSteps(self, s: str) -> int:
        total, ones = 0, 0

        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
            else:
                total += ones
        return total
        