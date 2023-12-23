class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        flag = False
        m = len(strs)
        n = len(strs[0])

        for j in range(n):
            for i in range(m - 1):
                flag = False
                if strs[i][j] > strs[i + 1][j]: 
                    count += 1
                    flag = True
                    break
            if flag:
                continue
        return count

                