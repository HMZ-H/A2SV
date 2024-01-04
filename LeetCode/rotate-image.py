import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix.reverse()
        tra = list(zip(*matrix))
        res = [list(i) for i in tra]
        for i in range(len(matrix)):
            matrix[i] = res[i]

    

        