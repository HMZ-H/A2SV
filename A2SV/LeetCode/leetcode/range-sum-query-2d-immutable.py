class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cols = len(matrix[0]) + 1
        self.rows = len(matrix) + 1
        self.prefix_sum = [[0 for _ in range(self.cols)] for _ in range(self.rows)] 
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2 + 1][col2 + 1] -self.prefix_sum[row1][col2 + 1] - self.prefix_sum[row2 + 1][col1] + self.prefix_sum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)