class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        lookup = defaultdict(int)
        for i in range(len(fronts)):
            lookup[fronts[i]] += 1
            lookup[backs[i]] += 1
        
        i = 0
        while i < len(fronts):
            if fronts[i] == backs[i] and fronts[i] in lookup:
                del lookup[fronts[i]]
            i += 1
        return min(lookup.keys()) if len(lookup) > 0 else 0
        return 0