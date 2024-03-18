class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.votes = defaultdict(int)
        self.leadings = []
        max_vote = 0

        for i in range(len(persons)):
            t = times[i]
            p = persons[i]
            self.votes[p] += 1

            if not self.leadings:
                self.leadings.append(p)
                max_vote = 1
            elif self.votes[p] >= max_vote:
                self.leadings.append(p)
                max_vote = self.votes[p]
            else:
                self.leadings.append(self.leadings[-1])
        

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1
        return self.leadings[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)