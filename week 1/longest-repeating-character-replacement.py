class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        i = 0
        j = 0
        max_len = 0
        max_occurence = 0

        while j < len(s):
            count[s[j]] += 1
            max_occurence = count[max(count, key = lambda x: count[x])]
            j += 1
            while j - i - max_occurence > k:
                count[s[i]] -= 1
                max_occurence = count[max(count, key = lambda x: count[x])]
                i += 1
            max_len = max(max_len, j - i)
        return max_len
        