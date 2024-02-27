class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index, strs):
            k = 0
            string = ""
            
            while index < len(strs):
                if strs[index] == "[": 
                    idx , SubStr = decode(index + 1, strs)
                    string += (k * SubStr)
                    k , index = 0 , idx
                elif strs[index].isdigit():
                    k = k * 10 + int(strs[index])
                elif strs[index] == "]":
                    return index, string
                else:
                    string += strs[index]
                
                index +=1
            return index, string
                
                
        _ , decodedStr = decode(0,s)
        return decodedStr
        