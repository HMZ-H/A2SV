class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = ten = 0
        for i in bills:
            
            if i == 5:
                fives +=1
            elif i == 10 and fives:
                fives -=1
                ten +=1
            elif i == 20 and fives and ten:
                fives -= 1
                ten -=1
            elif i == 20 and fives >= 3:
                fives -= 3
            else:
                return False
        return True
        