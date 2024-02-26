class Solution:
    def power(self, num, n, mod):
            if n == 1:
                return num
            if n < 1:
                return 1
            val = self.power(num, n // 2, mod)
            if n % 2 == 0:
                return (val * val) % mod
            return (val * val * num) % mod
    def countGoodNumbers(self, n: int) -> int:

        modulo = 10 ** 9 + 7
        if n%2 == 0:
            return ((self.power(4, n//2, modulo))*(self.power(5, n//2,modulo)))%(modulo)
        else:
            return ((self.power(4, n//2, modulo))*(self.power(5, 1+n//2 ,modulo)))%(modulo)
        

        


        