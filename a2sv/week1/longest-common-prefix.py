class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ans = ""
        l = float("inf")
        for strr in strs:
            l = min(l, len(strr))
        for i in range(l):
            a = strs[0]
            for strr in strs:
                if a[i] != strr[i]:
                    return ans
            ans += a[i]
        return ans



        