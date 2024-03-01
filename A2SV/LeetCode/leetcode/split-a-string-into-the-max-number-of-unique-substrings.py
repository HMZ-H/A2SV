class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # res = []
        res = float('-inf')
        def backt(index, path=[]):
            nonlocal res
            if len(s) <= index:
                res = max(res, len(path))
                return
            for i in range(index, len(s)):
                curr = s[index:i+1]
                if curr not in path:
                    path.append(curr)
                    backt(i+1, path)
                    path.pop()
        
        backt(0)
        return res

