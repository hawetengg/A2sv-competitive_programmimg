# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        index = 1
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                index = mid
                right = mid - 1
            elif not isBadVersion(mid):
                left = mid + 1
                
        return index