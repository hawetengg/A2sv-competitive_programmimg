class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        look_upS1 = Counter(s1)
        look_upS2 = Counter(s2[:len(s1)])

        if look_upS1 == look_upS2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            look_upS2[s2[r]] += 1
            look_upS2[s2[l]] -= 1
            if look_upS2[s2[l]] == 0:
                del look_upS2[s2[l]]
            l += 1
            if look_upS2 == look_upS1:
                return True
















        