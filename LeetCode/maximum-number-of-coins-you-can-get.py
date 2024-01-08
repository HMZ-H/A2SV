class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_coin = 0
        piles.sort()
        for i in range(len(piles)//3):
            max_coin += piles[-2 - 2*i]
        return max_coin
        