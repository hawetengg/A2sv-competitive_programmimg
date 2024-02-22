class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        check = ""

        for s in path + '/':
            if s == '/':
                if check == '..':
                    if stack:
                        stack.pop()
                elif check != "" and check != '.':
                    stack.append(check)
                check = ""
            else:
                check += s
        return '/' + '/'.join(stack)
            
        