class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        flag = True
        i = 0
        j = len(skill) - 1
        total = skill[i] + skill[j]
        ans = skill[i] * skill[j]
        if len(skill) == 2:
            return skill[i] * skill[j]
        i += 1
        j -= 1
        while (i < j):
            if skill[i] + skill[j] == total:
                ans += (skill[i] * skill[j])
                i += 1
                j -= 1
            else:
                flag = False
                break
        if flag:
            return ans
        else:
            return -1

        