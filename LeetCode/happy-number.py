class Solution:
    def isHappy(self, n: int) -> bool:
        lis_set = set()
        while n != 1:
            if n in lis_set:
                return False
            lis_set.add(n)
            n = sum([int(n)**2 for n in str(n)])
        else:
            return True
        
            

        