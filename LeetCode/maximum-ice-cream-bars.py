class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cout = 0
        for i in range(len(costs)):
            if coins - costs[i] >= 0:
                cout +=1
                coins -= costs[i]
            
        return cout

        