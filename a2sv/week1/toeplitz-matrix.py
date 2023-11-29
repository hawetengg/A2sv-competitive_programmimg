class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[0])):
                if(matrix[x][y] != matrix[x-1][y-1]):
                    return False
        return True
        