class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lookup = defaultdict(int)
        for num in arr:
            lookup[num] += 1
        n = len(arr) / 4
        for x, i in lookup.items():
            if i > n:
                return x
        return 0
        

        