class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        summ = 0
        count = 0
        for i in range(len(costs)):
            summ += costs[i]
            count += 1
            if summ == coins:
                return count
            elif summ > coins:
                return count - 1
        return count
        