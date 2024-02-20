class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # for i in range(1, rowIndex+1):
        #     res = prev*(rowIndex-i+1)//i
        #     ans.append(res)
        #     prev = res
        ans = [1]
        def rec( n,i):
            if i>n:
                return ans
            val = ans[-1] * (n -i + 1)//i
            ans.append(val)
           
            return rec(n, i+1)
        return rec(rowIndex, 1)

        