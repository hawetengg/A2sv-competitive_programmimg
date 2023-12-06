class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        strs1 = str(''.join(word1))
        strs2 = str(''.join(word2))
        if strs1 == strs2:
          return True
        else:
          return False
        