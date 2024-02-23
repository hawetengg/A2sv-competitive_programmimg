class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        rowMax = []
        colMax = []

        for row in grid:
            rowMax.append(max(row))
        for i in range(len(grid)):
            column = []
            for j in range(len(grid[0])):
                column.append(grid[j][i])
            colMax.append(max(column))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff = abs(grid[i][j]- min(rowMax[i], colMax[j]))
                total += diff
        return total
                


        