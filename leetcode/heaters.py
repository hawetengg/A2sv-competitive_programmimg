class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0
        right = max(max(houses), max(heaters))
        minRadius = right

        def checkRadius(mid):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if mid >= (abs(houses[i] - heaters[j])):
                    i += 1
                else:
                    j += 1
            return i == len(houses)

        while left <= right:
            mid = (left + right) // 2
            if checkRadius(mid):
                minRadius = min(minRadius, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minRadius




        