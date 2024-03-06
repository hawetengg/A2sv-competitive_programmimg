class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        val = letters[0]

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                val = letters[mid]
                right = mid - 1
            else:
                left = mid + 1

        return val
                



        