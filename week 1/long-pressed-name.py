class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0] or len(name) > len(typed):
            return False
        i = 0
        j = 0
        while not(i == len(name) and j == len(typed)):
            if (i < len(name) and j < len(typed) and name[i] == typed[j]):
                i += 1
                j += 1
            elif (j < len(typed) and typed[j] == name[i-1]):
                j += 1
            else:
                return False
        return True