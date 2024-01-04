class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        res = 0
        i  = 0
        for process in processorTime:
            res = max(res, process+tasks[i])
            i += 4
        return res
        