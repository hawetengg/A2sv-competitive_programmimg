class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(len(s))
        output = ""
        index = 0
        for i in range(len(s)):
            if spaces[index] == i:
                output += " "
                index += 1
            output += s[i]
        return output