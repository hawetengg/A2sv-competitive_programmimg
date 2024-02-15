class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        arr = []
        result = n * [0]

        for i, j, num in bookings:
            arr.append((i - 1, num))
            arr.append((j, -num))

        arr.sort()
        curr, prev = 0, 0

        for i, num in arr:
            for j in range(prev, i):
                result[j] += curr
            prev = i
            curr += num
        return result


        
        
        