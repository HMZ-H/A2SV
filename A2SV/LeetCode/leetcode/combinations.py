class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lis = []
        def backt(start, path):
            if len(path) == k:
                lis.append(path[:])
                return
            for num in range(start, n+1):
                path.append(num)
                backt(num + 1, path)
                path.pop()
            
        backt(1, [])
        # print(lis)
        return lis
        
        