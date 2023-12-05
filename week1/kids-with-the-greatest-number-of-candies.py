class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        maxx = candies[0]
        
        for num in candies:
            if num > maxx:
                maxx = num
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxx:
                val = True
                output.append(val)
            elif candies[i] + extraCandies < maxx:
                val = False
                output.append(val)
        return output
