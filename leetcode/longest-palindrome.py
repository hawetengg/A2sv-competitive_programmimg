class Solution:
    def longestPalindrome(self, s: str) -> int:
        look_up = Counter(s)
        ans = 0
        odd_found = False
        arr = []

        
        for key, value in look_up.items():
            arr.append(value)

        arr.sort(reverse = True)

        for value in arr:
            if value % 2 == 0:
                ans += value
            else:
                if odd_found == False:
                        ans += value
                        odd_found = True
                else:
                    ans += value - 1
        return ans


        