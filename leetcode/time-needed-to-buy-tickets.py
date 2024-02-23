class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        time = 0

        for i in range(len(tickets)):
            queue.append(i)
        
        while queue:
            index = queue.popleft()
            if tickets[index] > 0:
                tickets[index] -= 1
                time += 1
            if tickets[index] > 0:
                queue.append(index)
            if tickets[k] == 0:
                return time


        