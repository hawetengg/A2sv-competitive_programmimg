class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []

        for i in range(len(points)):
            arr.append(points[i][0])
        arr.sort()
        res = 0
        for j in range(1, len(arr)):
            res = max(res, arr[j] - arr[j - 1])
        return res
        