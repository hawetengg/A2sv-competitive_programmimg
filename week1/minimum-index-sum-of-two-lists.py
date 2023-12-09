class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        len1 = len(list1)
        len2 = len(list2)
        result = []
        min_index = len1 + len2
        for i in range(len1):
            for j in range(len2):
                if list1[i] == list2[j]:
                    if i + j == min_index:
                        result.append(list1[i])
                    if i + j < min_index:
                        result = []
                        result.append(list1[i])
                        min_index = i + j
        return result