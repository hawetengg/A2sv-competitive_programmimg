class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        ans = []
        
        for i in range(len(points)):
            distance =  math.sqrt( ( points[i][0] ) **2 + ( points[i][1] ) **2  )
            dist.append([distance,points[i]])
        
        dist.sort()
        
        for i in range(k):
            ans.append(dist[i][1])
        
        return ans