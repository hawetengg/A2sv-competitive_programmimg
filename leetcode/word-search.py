class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mySet = set()

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            if word[k] != board[i][j] or (i, j) in mySet:
                return False
            
            mySet.add((i, j))

            ans = (backtrack(i, j + 1, k + 1) or backtrack(i + 1, j, k + 1) or 
            backtrack(i, j - 1, k + 1) or 
            backtrack(i - 1, j, k + 1))

            mySet.remove((i,j))

            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False


        
        