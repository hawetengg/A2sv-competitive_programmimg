class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        r = 0
        n = len(mat)
        for i in range(n):
            r -= 1
            summ += mat[i][i] 
            summ += mat[i][r]
        if n%2:
            summ -= mat[n//2][n//2]
        return summ