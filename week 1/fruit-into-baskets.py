class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        look_up = {}
        max_length = 0
        left = 0

        for right, fruit in enumerate(fruits):
            look_up[fruit] = right

            while len(look_up) > 2:
                if look_up[fruits[left]] == left:
                    del look_up[fruits[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length