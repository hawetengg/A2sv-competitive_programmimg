class Solution:
    def smallestNumber(self, num: int) -> int:
        if num // 10 == 0:
            return num
        if num < 0:
            sign =- 1
        else:
            sign = 1
        num = abs(num)    
        if sign == -1:
            s = sorted(str(num),reverse=True)
            return sign * int("".join(s))
        else:
            s = sorted(str(num))
            zeros = s.count('0')
            if zeros != 0:
                s[0], s[zeros]=s[zeros], s[0]
            return sign*int("".join(s))