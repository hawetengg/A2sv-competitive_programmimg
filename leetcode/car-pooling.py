class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []

        for people, start, end in trips:
           arr.append((start, people))
           arr.append((end, -people))
        arr.sort()
        for pos, people in arr:
            capacity -= people
            if capacity < 0:
                return False 
        return True