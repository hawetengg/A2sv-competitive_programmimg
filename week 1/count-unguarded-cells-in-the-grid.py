class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = [[0]*n for _ in range(m)]
        for i,j in walls:
            arr[i][j] = 2
        for i,j in guards:
            arr[i][j] = 2
        for i,j in guards:
            for l in range(j-1,-1,-1):
                if self.checkWall(i,l,arr):
                    break    
                arr[i][l] = 1
            for r in range(j+1,n):
                if self.checkWall(i,r,arr):
                    break
                arr[i][r] = 1
            for u in range(i-1,-1,-1):
                if self.checkWall(u,j,arr):
                    break
                arr[u][j] = 1
            for d in range(i+1,m):
                if self.checkWall(d,j, arr):
                    break
                arr[d][j] = 1
        return sum(row.count(0) for row in arr)
        
    def checkWall(self, i, j, arr):
        if arr[i][j] ==2:
            return True