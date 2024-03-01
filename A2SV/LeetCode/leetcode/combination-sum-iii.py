class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backt(index, path=[], sums=0):
            print(path)
            if len(path) == k and sums == n:
                res.append(path[:])
                return
            if len(path) >= k or sums > n:
                return 
            for i in range(index, min(n+1, 10)):
                if sums <= n:
                    path.append(i)
                    sums +=i
                    backt(i + 1, path, sums)
                    path.pop()
                    sums-=i
        backt(1)
        return res        