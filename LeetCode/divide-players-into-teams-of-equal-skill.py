class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill)-1
        chem = 0
        prev = skill[left] + skill[right]
        while right > left:
            total_skill = skill[left] + skill[right]
            if prev != total_skill:
                return -1
            chem += skill[left] * skill[right]
            
            left +=1
            right -=1
       
        return chem
        
        