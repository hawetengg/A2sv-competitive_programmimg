class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse = True)
        
        i = 0
        while i < len(deck):
            if not queue:
                queue.append(deck[i])
            else:
                num = queue.pop()
                queue.appendleft(num)
                queue.appendleft(deck[i])
            i += 1

        return list(queue)
        