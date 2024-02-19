class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        bestTime = 0

        for i in range(0, len(customers)):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < 0:
                penalty = 0
                bestTime = i + 1
        return bestTime


        