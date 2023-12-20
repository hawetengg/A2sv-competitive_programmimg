class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a = len(matrix) 
        b = len(matrix[0])

        output = [[0] * a for _ in range(b)]
        for i in range(b):
            for j in range(a):
                output[i][j] = matrix[j][i]
        return output
        