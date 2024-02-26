class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []

        def recursion(rowIndex):
            if rowIndex == 0:
                return [1]
            val = recursion(rowIndex - 1)
            output.append(val)
            arr = []
            arr.append(1)
            for j in range(len(output[-1]) - 1):
                arr.append(output[-1][j] + output[-1][j + 1])
            arr.append(1)
            output.append(arr)
            return output[-1]
        x = recursion(rowIndex)
        return x