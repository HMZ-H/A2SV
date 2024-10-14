# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:

    def knapSack(self, W, wt, val):
        n = len(wt)
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):

                if i == 0 or w == 0:
                    K[i][w] = 0

                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                                  K[i - 1][w])

                else:
                    K[i][w] = K[i - 1][w]

        return K[n][W]
