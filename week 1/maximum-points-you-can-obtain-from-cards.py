class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        total = sum(cardPoints[r:])
        max_score = total

        while r < len(cardPoints):
            total += cardPoints[l]
            total -= cardPoints[r]
            max_score = max(max_score, total)
            l += 1
            r += 1
        return max_score


        