class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        strs = ""
        while i < len(s):
            strs += s[i:i + k][::-1]
            strs += s[i + k: i + k + k]
            i += k + k
        return strs

    
            