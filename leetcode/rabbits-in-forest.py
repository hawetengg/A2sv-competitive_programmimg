class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = collections.defaultdict(int)

        for rabbit in answers:
            counts[rabbit] += 1
        res = 0
        for key in counts.keys():
            count = counts[key]
            num = ((count - 1) // (key + 1)) + 1
            res += num * (key + 1)
        return res
        