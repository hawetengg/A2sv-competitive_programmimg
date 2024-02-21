class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []

        for i in s:
            if i == '(':
                arr.append('(')
            else:
                if arr and arr[-1] == '(':
                    arr.pop()
                else:
                    arr.append(')')

        return len(arr)
                
        