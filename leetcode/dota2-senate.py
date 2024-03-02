class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D = deque()
        R = deque()

        for index, value in enumerate(senate):
            if value == "D":
                D.append(index)
            else:
                R.append(index)

        while R and D:
            turnR = R.popleft()
            turnD = D.popleft()

            if turnR > turnD:
                D.append(turnR + len(senate))
            else:
                R.append(turnD + len(senate))

        return "Dire" if D else "Radiant" 
        