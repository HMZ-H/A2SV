class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        left = 0     
        right = 0      
        while left <= len(name) and right < len(typed):
            if left < len(name) and typed[right] == name[left]:
                right += 1
                left += 1
            elif typed[right] == name[left-1] and left != 0:
                right += 1
            else:
                return False
            
        return left == len(name) and right == len(typed)
        

        