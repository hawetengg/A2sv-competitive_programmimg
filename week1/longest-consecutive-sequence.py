class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_num = list(set(nums))
        new_num.sort()
        count = 1
        max_count = 1
        i = 0
        if len(new_num) == 0:
            max_count = 0
        else:
            while i < len(new_num) - 1:
                if new_num[i + 1] == new_num[i] + 1:
                    count += 1
                    if count >= max_count:
                        max_count = count
                    i += 1
                else:
                    count = 1
                    i += 1
                    
        return max_count
            


        
        