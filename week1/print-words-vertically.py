class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        s = s.split(" ")
        maxLen = 0
        for word in s:
            if len(word) > maxLen:
                maxLen = len(word)
        for i in range(maxLen):
            new_word = []
            for word in s:
                if i >= len(word):
                    new_word.append(" ")
                else:
                    new_word.append(word[i])
            joined_word = ''.join(new_word).rstrip()
            result.append(joined_word)
        return result
        
        
        