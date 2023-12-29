class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        new={i[-1:]:i[:-1] for i in s}
        n=dict(sorted(new.items()))
        
        return " ".join(n.values())