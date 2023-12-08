class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dictt = {}

        for i , pos in enumerate(indices):
            dictt[pos] = s[i]
        output = ""
        for i in range(len(s)):
            output += dictt[i]
        return output


           
        