class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        if start > destination:
            start, destination = destination, start
        for i in range(start, destination):
            sum1 += distance[i]
        for i in range(destination, len(distance)):
            sum2 += distance[i]
        for i in range(0, start):
            sum2 += distance[i]
        minlen = min(sum1, sum2)
        return minlen
        