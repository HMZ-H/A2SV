class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        dic = {'(':')', '{':'}','[':']'}
        for char in s:
            if char in dic:
                lis.append(char)
            elif not lis:
                return False
            else:
                if dic[lis.pop()] != char:
                    return False
        return not lis
          
        
        return lis == []
            

        