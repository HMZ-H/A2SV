class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.W = len(matrix[0])+1   
        self.H = len(matrix)+1
        self.ps = [[0 for _ in range(self.W)] for _ in range(self.H)]
        for i in range(1, self.H):
            for j in range(1, self.W):
                self.ps[i][j] = self.ps[i-1][j] + self.ps[i][j-1] - self.ps[i-1][j-1] + matrix[i-1][j-1]

    # ps[x][y] = matrix[0][0]+...+matrix[x-1][y-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.ps[row2+1][col2+1] - self.ps[row1][col2+1] - self.ps[row2+1][col1] + self.ps[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)