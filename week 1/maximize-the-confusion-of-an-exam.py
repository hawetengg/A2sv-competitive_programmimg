class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_countF = 0
        max_countT = 0
        newK = k

        l1 = 0
        for r1 in range(len(answerKey)):
            if answerKey[r1] == 'F':
                k -= 1
                while k < 0:
                    if answerKey[l1] == 'F':
                        k += 1
                    l1 += 1
            max_countT = max(max_countT, r1 - l1 + 1)
        k = newK
        l2 = 0
        for r2 in range(len(answerKey)):
            if answerKey[r2] == 'T':
                k -= 1
                while k < 0:
                    if answerKey[l2] == 'T':
                        k += 1
                    l2 += 1
            max_countF = max(max_countF, r2 - l2 + 1)
        result = max(max_countF, max_countT)
        return result

        