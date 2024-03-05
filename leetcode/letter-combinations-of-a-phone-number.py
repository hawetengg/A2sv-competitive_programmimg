class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        chars = {"2": "abc", "3": "def", "4":"ghi", "5": "jkl", 
        "6": "mno", "7": "pqrs", "8":"tuv", "9":"wxyz"}

        def backtrack(i, strs):
            if len(strs) == len(digits):
                ans.append(strs)
                return

            for charr in chars[digits[i]]:
                backtrack(i + 1, strs + charr)

        if digits:
            backtrack(0, "")

        return ans
        