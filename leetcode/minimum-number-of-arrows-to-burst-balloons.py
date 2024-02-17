class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        prev = points[0]
        total = 1
        for i, j in points[1:]:
            if i > prev[1]:
                total += 1
                prev = [i, j]
            else:
                prev[1] = min(prev[1], j)
        return total
        