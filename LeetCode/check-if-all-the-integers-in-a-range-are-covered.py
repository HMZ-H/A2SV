class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        mat= []
        for i,j in ranges:
            mat.extend(list(range(i,j+1)))
        
        for i in range(left, right+1):
            if i not in mat:
                return False
        return True
        