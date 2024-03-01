class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        look_up = {}
        ans = [-1] * len(nums)
        
        for i in range(2):
            for index, value in enumerate(nums):
                while stack and value > stack[-1][1]:
                    num = stack.pop()
                    ans[num[0]] = value
                stack.append((index, value))

        return ans
        