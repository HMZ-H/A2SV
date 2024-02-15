class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix) 
        cols = len(matrix[0])

        prefixSum = [[0 for i in range(cols+1)] for i in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols):
                prefixSum[i+1][j+1] = prefixSum[i+1][j] + prefixSum[i][j+1] - prefixSum[i][j] + matrix[i][j]
        cout = 0
        for i in range(1, rows+1):
            for j in range(i, rows +1):

                dic = defaultdict(int)
                dic[0] = 1
                for c in range(1, cols + 1):
                    curr_sum = prefixSum[j][c] - prefixSum[i -1][c]
                    cout += dic[curr_sum - target]
                    dic[curr_sum]  += 1

        return cout
        