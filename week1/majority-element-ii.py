class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = []
        new_set = set(nums)

        for num in new_set:
            if nums.count(num) > length / 3:
                result.append(num)
        return result
        