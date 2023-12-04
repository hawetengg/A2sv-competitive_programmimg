class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        sum = 0.0
        leng = len(salary)
        for i in range(1, leng - 1):
            sum += salary[i]
        avg = sum / (leng - 2) 
        return avg
