class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        look_up = {}
        min_value = len(cards) + 1

        for i in range(len(cards)):
            if cards[i] not in look_up:
                look_up[cards[i]] = i
            else:
                min_value = min(min_value, i - look_up[cards[i]] + 1)
                look_up[cards[i]] = i
        if min_value == len(cards) + 1:
            return -1
        else:
            return min_value

    """
    class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        look_up = {}
        min_value = len(cards) + 1

        for i in range(len(cards)):
            if cards[i] not in look_up:
                look_up[cards[i]] = i
            else:
                min_value = min(min_value, i - look_up[cards[i]])

        if min_value == len(cards) + 1:
            return -1
        else:
            return min_value
    """
                

        