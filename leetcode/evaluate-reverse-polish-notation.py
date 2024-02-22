class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i == "+" and stack:
                ans = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ans)                                           
            elif i == "*" and stack:
                ans = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif i == "-" and stack:
                ans = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif i == "/" and stack:
                ans = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(ans))
            else:
                stack.append(int(i))
        return int(ans)


        