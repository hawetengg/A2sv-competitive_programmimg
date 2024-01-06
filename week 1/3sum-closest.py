class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(target - ans):
                    ans = s
                if target == s:
                    return s
                if s > target:
                    r -= 1
                else:
                    l += 1

        return ans