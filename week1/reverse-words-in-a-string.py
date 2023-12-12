class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        n = len(strs)
        
        return ' '.join(strs[::-1])