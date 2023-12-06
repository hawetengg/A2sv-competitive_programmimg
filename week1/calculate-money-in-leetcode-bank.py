class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ = 0
        x = n // 7
        y = n % 7
        if n < 7:
          return sum(range(1, n + 1))

        for i in range(1, x + 2):
            if i < x + 1:
                summ += sum(range(i, i + 7))
            if i == x + 1:
                summ += sum(range(i, i + y))
        return summ
             
        