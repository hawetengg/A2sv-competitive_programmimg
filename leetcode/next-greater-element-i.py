class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        look_up = {}
        stack = []
        ans = [-1] * len(nums1)

        for index, value in enumerate(nums1):
            look_up[value] = index

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                ans[look_up[stack.pop()]] = nums2[i]
            if nums2[i] in nums1:
                stack.append(nums2[i])
        
        return ans



        

            
        
        