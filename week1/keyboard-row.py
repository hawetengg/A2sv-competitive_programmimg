class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        strs2 = "asdfghjkl"
        strs1 = "qwertyuiop"
        strs3 = "zxcvbnm"
        output = []
        for word in words:
            arr = []
            for i in range(len(word)):
                if word[i].lower() in strs1:
                    arr.append(1)
                elif word[i].lower() in strs2:
                    arr.append(2)
                else:
                    arr.append(3)
            if max(arr) == min(arr):
                output.append(word)
        return output
            
                    
                
            
      


        