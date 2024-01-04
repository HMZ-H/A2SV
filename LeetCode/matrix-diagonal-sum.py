class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = []
        n = len(mat)
        for i in range(len(mat)):
            sums.append(mat[i][i])
            sums.append(mat[i][~i])

        ans = sum(sums)
        if n%2 == 1:
            mid = n//2
            ans -= mat[mid][mid]

        return ans
      
        