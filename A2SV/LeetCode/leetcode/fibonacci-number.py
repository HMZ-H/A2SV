class Solution:
    def fib(self, n: int, memo = {}) -> int:
        if n in memo:
            return memo[n]
        if n in [0,1]:
            return n
        
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]
        