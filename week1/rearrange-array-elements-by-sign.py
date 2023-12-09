class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = []
        left, right = [], []
        for i in nums:
            if i < 0:
                left.append(i)
            else:
                right.append(i)
        for i in range(int(len(nums) / 2)):
            output.append(right[i])
            output.append(left[i])
        return output 
        