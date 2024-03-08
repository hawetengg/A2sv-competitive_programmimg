class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def cur(n, k):
            if n == 1:
                return 0
            val = 2 ** (n - 2)
            if val >= k:
                return cur(n - 1, k)
            else:
                print(k - val)
                return 1 + cur(n - 1, k - val)
        s=cur(n, k)
        return 1 if s % 2 else 0
