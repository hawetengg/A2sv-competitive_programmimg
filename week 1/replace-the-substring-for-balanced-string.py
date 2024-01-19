class Solution:
    def balancedString(self, s: str) -> int:
        char_count = Counter(s)
        l = 0
        new_len = len(s) // 4
        ans = len(s)

        for r in range(len(s)):
            char_count[s[r]] -= 1
            while l < len(s) and char_count['Q'] <= new_len and char_count['W'] <= new_len and char_count['E'] <= new_len and char_count['R'] <= new_len:
                ans = min(ans, r - l + 1)
                char_count[s[l]] += 1
                l += 1
        return ans

        