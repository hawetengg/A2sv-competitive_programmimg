class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        is_up = True
        m = len(mat)
        n = len(mat[0])
        def inbound(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
        i, j = 0, 0
        while (inbound(i, j)):
            ans.append(mat[i][j])
            if is_up:
                if inbound(i - 1, j + 1):
                    i -= 1
                    j += 1
                elif inbound(i, j + 1):
                    j += 1
                    is_up = False
                else:
                    i += 1
                    is_up = False
            else:
                if inbound(i + 1, j - 1):
                    i += 1
                    j -= 1
                elif inbound(i + 1, j):
                    i += 1
                    is_up = True
                else:
                    j += 1
                    is_up = True
        return ans





        

        