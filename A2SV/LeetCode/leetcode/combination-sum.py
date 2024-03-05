class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        lis = []
        def backt(index, path = [] ,sm = 0):
            if sm == target:
                lis.append(path[:])
                return 
            # if len(path) > 150:
            #     return

            for i in range(index, len(candidates)):
                if sm + candidates[i] <= target:
                    sm += candidates[i]
                    path.append(candidates[i])
                    backt(i, path, sm)
                    path.pop()
                    sm -= candidates[i]
        backt(0)
        return lis