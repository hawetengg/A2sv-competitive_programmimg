class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r:])
        max_count = total

        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            max_count = max(max_count, total)
            l += 1
            r += 1
        return max_count
        