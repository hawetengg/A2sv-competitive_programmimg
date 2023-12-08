class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)

        for i in range(len(nums) - 2):
            base = nums[i]
            side_1 = nums[i+1]
            side_2 = nums[i + 2]
            if side_1 + side_2 > base:
                return base + side_1 + side_2
        return 0