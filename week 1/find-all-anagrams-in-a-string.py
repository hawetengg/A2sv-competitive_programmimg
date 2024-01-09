class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        look_upP = defaultdict(int)
        look_upS = defaultdict(int)

        for i in range(len(p)):
            look_upP[p[i]] += 1
        for i in range(min(len(p), len(s))):
            look_upS[s[i]] += 1
        
        i = 0
        j = len(p)

        while(j < len(s)):
            if look_upP == look_upS:
                ans.append(i)
            look_upS[s[i]] -= 1
            if look_upS[s[i]] == 0:
                del look_upS[s[i]]
            i += 1
            look_upS[s[j]] += 1
            j += 1
        if look_upS == look_upP:
            ans.append(i)
        
        return ans
        

