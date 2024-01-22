class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)
        result = []

        for start, end, direction in shifts:
            if direction == 0:
                prefix[start] -= 1
                prefix[end + 1] += 1
            else:
                prefix[start] += 1
                prefix[end + 1] -= 1
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        for i, l in enumerate(s):
            shift = (ord(l) - ord('a') + prefix[i]) % 26
            new_letter = chr(shift + ord('a'))
            result.append(new_letter)
        return "".join(result)


        