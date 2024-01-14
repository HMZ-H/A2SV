class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # left, right = 0
        res = []
        for x,y in firstList :
            for i,j in secondList:
                if x >= i and x <= j and y>=i and y<=j :
                    res.append([x,y])
                elif x >= i and x <= j and y >= i and y>=j:
                    res.append([x,j])
                elif x <= i and x <= j and y >= i and y <= j:
                    res.append([i,y])
                elif x <= i and x <= j and  y>=i and y>= j:
                    res.append([i,j])
                
        return res
        