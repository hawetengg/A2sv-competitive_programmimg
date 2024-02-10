class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])

        self.summ = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(row):
            total = 0
            for j in range(col):
                total += matrix[i][j]
                up = self.summ[i][j + 1]
                self.summ[i + 1][j + 1] = total + up
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        up = self.summ[row1 - 1][col2]
        br = self.summ[row2][col2]
        tl = self.summ[row1 - 1][col1 - 1]
        l = self.summ[row2][col1 - 1]
        return br - up - l + tl

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)