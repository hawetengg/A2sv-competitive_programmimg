class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr)-1):
            if arr[i] >= arr[i + 1]:
                break
        for j in range(len(arr)-1, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
        return i == j