class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                break

        mat_index = mid
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if target == matrix[mat_index][m]:
                return True
            elif target > matrix[mat_index][m]:
                l = m + 1
            else:
                r = m - 1

        return False