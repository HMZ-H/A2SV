class Solution:
    def splitString(self, s: str) -> bool:
        # res = []
        n = len(s)
        def backt(index, path=[]):
            if index == n:
                # res.append(path)
                if len(path) >= 2:
                    return True
                return False

            for i in range(index, n):
                num = int(s[index:i+1])
                if not path or path[-1] - num == 1:
                    path.append(num)
                    res = backt(i+1, path)
                    path.pop()
                    if res:
                        return res
            return False
       
        return backt(0)