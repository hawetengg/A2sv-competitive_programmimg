class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        start, end = 0, 0
        answer = []

        for index, value in enumerate(s):
            last_index[value] = index

        for index, value in enumerate(s):
            end = max(end, last_index[value])
            if end == index:
                answer.append(end - start + 1)
                start = index + 1

        return answer


        
