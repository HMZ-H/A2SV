class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec( n):
            if n == 1:
                return '0'
            l = rec(n-1)
            s = ''
            for i in range(len(l)):
                if l[i] == '0':
                    s+='1'
                else:
                    s+='0'
            return l + "1" + s[::-1]
        return rec(n)[k-1]
        