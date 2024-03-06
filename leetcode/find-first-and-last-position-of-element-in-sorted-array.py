class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_idx, max_idx = -1, -1
        ans = []
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                min_idx = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        ans.append(min_idx)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                max_idx = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        ans.append(max_idx)

        return ans
        

        