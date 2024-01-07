class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            if not (second[1] < first[0] or second[0] > first[1]):   
                res.append([max(second[0], first[0]), min(second[1], first[1])])
            if first[1] < second[1]:
                i += 1
            else:
                j += 1
        return res
        