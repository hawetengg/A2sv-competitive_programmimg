class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        total = sum(x for x in nums if x % 2 == 0)
        for num, i in queries:
            prev = nums[i]
            nums[i] += num

            if prev % 2 == 0:
                if nums[i] % 2 == 0:
                    total += num
                else:
                    total -= prev
            else:
                if nums[i] % 2 == 0:
                    total += nums[i]
            ans.append(total)
        return ans 
        