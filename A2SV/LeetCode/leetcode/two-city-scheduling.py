class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        costs.sort(key = lambda x: x[0] - x[1])
        mid = len(costs)//2
        # print(costs)
        for i in range(mid):
            total += costs[i][0] + costs[mid + i][1]
        return total

        