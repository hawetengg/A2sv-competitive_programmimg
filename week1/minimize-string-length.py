class Solution:
    def minimizedStringLength(self, s: str) -> int:
        output = [i for i in set(s)]
        return len(output)
