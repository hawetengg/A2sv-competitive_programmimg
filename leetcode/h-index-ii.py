class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1

        while left <= right:
            mid = (left + right) // 2
            diff = (len(citations) - mid)

            if diff == citations[mid]:
                return diff
            elif diff > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return len(citations) - left
            

        