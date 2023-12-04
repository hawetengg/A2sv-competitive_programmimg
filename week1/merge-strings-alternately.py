class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        final = ""
        i = 0
        j = 0
        minn = min(len(word1), len(word2))
        while i < minn and j < minn:
            final += word1[i]
            final += word2[j]
            i += 1
            j += 1
        if len(word1) > minn:
            final += word1[i:]
        if len(word2) > minn:
            final += word2[j:]
        return final

        
             