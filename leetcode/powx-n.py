class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1 / x
            ans = self.myPow(x, n)
            return ans
        else:
            y = n // 2
            ans = self.myPow(x, y)
            res = ans * ans
            if n % 2 == 0:
                return res
            else:
                return x * res