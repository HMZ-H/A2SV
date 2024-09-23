# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        buy = [0]*n
        sell = [0]*n
        cooldown = [0]*n
        buy[0] = -prices[0]
        
        
        for i in range(1,n):
            buy[i] = max(buy[i-1],cooldown[i-1]-prices[i])
            sell[i] = max(buy[i-1]+prices[i],sell[i-1])
            cooldown[i] = max(cooldown[i-1], sell[i-1])
        print(cooldown)
        return max(cooldown[n-1], sell[n-1])
        