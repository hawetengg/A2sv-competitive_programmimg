class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        stack = []
        ans = 0

        for index, value in enumerate(arr):
            while stack and value < stack[-1][-1]:
                idx, val = stack.pop()
                left = idx - stack[-1][0] if stack else idx + 1
                right = index - idx
                ans = (ans + val * left * right) % mod
            stack.append((index, value))

        for i in range(len(stack)):
            idx, value = stack[i]
            left = idx - stack[i - 1][0] if i > 0 else idx + 1
            right = len(arr) - idx
            ans = (ans + value * left * right) % mod

        return ans
        