class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        events = []
        N = len(nums)
        nums.sort(reverse = True)

        for start, end in requests:
            events.append((start, + 1))
            events.append((end + 1, -1))

        events.sort()
        counts = [-1] * (N + 1)
        current = 0
        last_index = 0

        for index, delta in events:
            current += delta
            counts[index] = current

        for index in range(N):
            if counts[index] == -1:
                if index == 0:
                    counts[index] = 0
                else:
                    counts[index] = counts[index - 1]
        s = reversed(sorted((count, index)for index, count in enumerate(counts)))
        total = 0
        for index, (count, _) in enumerate(s):
            if index < N:
                total += count * nums[index]
        return total % (10**9 + 7)

        