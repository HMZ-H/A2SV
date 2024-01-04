class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        
        res = []
        for i in dic:
            if i%2 == 0:
                res.extend(dic[i][::-1])
            else:
                res.extend(dic[i])
        return res

        