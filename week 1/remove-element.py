class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i, j = 0, len(nums)-1
        if(j == -1): 
            return 0
        while(i < j):
            if(nums[i] == val):
                while(i < j and nums[j] == val): 
                    j -= 1
                nums[i] = nums[j]
                j -= 1
                continue
            i += 1
        if nums[i] != val:
            return i + 1
        else:
            return i
        