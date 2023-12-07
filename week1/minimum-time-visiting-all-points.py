class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(points) - 1):
            val_1 = points[i]
            val_2 = points[i + 1]
            ans += max(abs(val_2[0] - val_1[0]), abs(val_2[1] - val_1[1]))
        return ans