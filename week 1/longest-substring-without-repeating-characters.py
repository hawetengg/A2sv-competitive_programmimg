class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        charSet = set()
        l = 0
        r = 0
        while l < len(s) and r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            count = max(count, r - l + 1)
            r += 1
        return count


        
        