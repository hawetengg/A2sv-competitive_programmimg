class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        win = []
        loss = []
        losses = defaultdict(int)

        for match in matches:
            losses[match[0]] = 0 
        for match in matches:
            losses[match[1]] += 1
        for team in losses:
            if losses[team] == 0:
                win.append(team)
            if losses[team] == 1:
                loss.append(team)
        win.sort()
        loss.sort()
        ans.append(win)
        ans.append(loss)
        return ans