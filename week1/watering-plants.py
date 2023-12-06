class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        cap = capacity
        steps = 0
        
        for i in range(len(plants)):
            if  capacity >= plants[i]:
                capacity -= plants[i]
                steps += 1
            else:
                steps += i
                capacity = cap
                steps += i + 1
                capacity -= plants[i]
        return steps





            