class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 10**9 + 7
        # return pow(5, (n+1)//2, mod) * pow(4, (n)//2, mod)%mod
        def pow(a, m):
            res = 1
            while m >0:
                if m & 1:
                    res *=a
                    res%=mod
                a = a*a% mod
                m = m >> 1
            return res
        m1 = pow(4, n//2)
        m2 = pow(5, n//2)
        m = m1*m2%mod
        if n%2 == 0:
            return m
        else:
            return m*5%mod
                
       
        