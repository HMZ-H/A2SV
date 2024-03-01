class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backt(index, path=[]):
            if len(path) > k:
                return 
            if len(path) == k and sum(path) == n:
                res.append(path[:])
            for i in range(index, 10):
                path.append(i)
                backt(i + 1, path)
                path.pop()
        backt(1)
        return res        