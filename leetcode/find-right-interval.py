class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        look_up = defaultdict(int)
        arr = []
        ans = [-1] * len(intervals)

        for index, interval in enumerate(intervals):
            look_up[interval[0]] = index
            arr.append(interval[0])
            
        arr.sort()

        def findRight(j, idx):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= j:
                    ans[idx] = look_up[arr[mid]]
                    right = mid - 1
                else:
                    left = mid + 1
        
        idx = 0
        for i, j in intervals:
            findRight(j, idx)
            idx += 1
        
        return ans
                

