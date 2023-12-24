class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n !=1:
            s = int(n/2)
            res+=s
            n = n-s
        return res

        