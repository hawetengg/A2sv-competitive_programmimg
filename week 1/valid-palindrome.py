class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = s.split()
        result = [''.join(char for char in word if char.isalnum()) for word in result]
        result = ''.join(result)
        result = result.lower()
        flag = True
        i = 0
        j = len(result) - 1

        while(i <= j):
            if result[i] == result[j]:
                i += 1
                j -= 1
            else:
                flag = False
                break
        if flag:
            return True
        else:
            return False