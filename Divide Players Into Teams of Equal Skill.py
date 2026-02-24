class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        n = len(skill)
        skill.sort()

        if n == 2:
            return skill[0] * skill[1]

        weak = 0
        strong = n - 1
        target_sum = skill[weak] + skill[strong]

        while weak < strong:

            if skill[weak] + skill[strong] != target_sum:
                return -1

            chemistry += skill[weak] * skill[strong]
            weak += 1
            strong -= 1 

        return chemistry    



