class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tra = list(zip(*matrix))
        res = []
        for i in tra:
            res.append(list(i))
        return res

        