class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        zero = 0
        one = s.count("1")

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            ans = max(ans, one + zero)

        return ans
        
        