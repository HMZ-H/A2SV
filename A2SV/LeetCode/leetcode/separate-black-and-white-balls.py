class Solution:
    def minimumSteps(self, s: str) -> int:

        
        cout, res = 0,0
        for i in range(len(s)-1,-1,-1):

            if s[i] == '0':
                cout +=1
            else:
                res +=cout
        return res

        