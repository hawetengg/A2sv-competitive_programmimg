class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(left, right, turn, score1, score2):
            if left > right:
                return score1 >= score2
            case1 = play(
                left + 1, 
                right, 
                2 if turn == 1 else 1,
                nums[left] + score1 if turn == 1 else score1,
                nums[left] + score2 if turn == 2 else score2
            )
            case2 = play(
                left, 
                right - 1,
                2 if turn == 1 else 1,
                nums[right] + score1 if turn == 1 else score1,
                nums[right] + score2 if turn == 2 else score2
            )
            if turn == 1:
                return case1 or case2
            else:
                return case1 and case2
        ans = play(0, len(nums) - 1, 1, 0, 0)
        return ans
        
        