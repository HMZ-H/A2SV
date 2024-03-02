class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        lis = []
        def backt(start, path):
            if path and len(digits) == len(path):
                lis.append(''.join(path[:]))
                return
            if start >= len(digits):
                return
            for i in dic[(digits[start])]:
                path.append(i)
                backt(start+1, path)
                path.pop()
        backt(0, [])
        return lis


            


            
        