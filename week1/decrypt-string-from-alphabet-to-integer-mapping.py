class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str

        """
        output = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                output += chr(int(s[i-2:i]) + 96)
                i -= 3
            else:
                output += chr(int(s[i]) + 96)
                i -= 1
        return output[::-1]
            
 