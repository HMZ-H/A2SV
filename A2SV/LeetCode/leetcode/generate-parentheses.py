class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        ls = ['(',  ')']
        def backtrack(index, path = [], open_bracket = 0):
            if open_bracket > n or len(path) - open_bracket > open_bracket:
                return 
            if len(path) == 2*n:
                if open_bracket == len(path) - open_bracket:
                    res.append(''.join(path[:]))
                return
            for i in range(2):
                if ls[i] == '(':
                    open_bracket+=1
                path.append(ls[i])
                backtrack(i+1, path, open_bracket)
                path.pop()
                if ls[i] == '(':
                    open_bracket-=1
        backtrack(0)
        
        return res