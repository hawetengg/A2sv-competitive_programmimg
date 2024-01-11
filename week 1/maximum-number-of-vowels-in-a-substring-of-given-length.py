class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = "aeiou"
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        l = 0
        for r in range(k, len(s)):
            if s[l] in vowels:
                count -= 1
            l += 1
            if s[r] in vowels:
                count += 1
            max_count = max(count, max_count)
        return max_count
        