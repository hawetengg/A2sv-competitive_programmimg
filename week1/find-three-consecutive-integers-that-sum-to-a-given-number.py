class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 == 0:
            a = num // 3
            return [a - 1, a, a + 1]
        return []

        