class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = 0

        for i in range(left, right + 1):
            for j, k in ranges:
                if i >= j and i <= k:
                    count += 1
                    break
        if count == (right - left + 1):
            return True
        return False