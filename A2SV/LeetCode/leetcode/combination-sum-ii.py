class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        fre = Counter(candidates)
        sets = []
        for i in candidates:
            if i not in sets:
                sets.append(i)
        # sets.sort()
        def backt(index, path=[]):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            for i in range(index, len(sets)):
                if fre[sets[i]] != 0:
                    path.append(sets[i])
                    fre[sets[i]] -= 1
                    backt(i, path)
                    path.pop()
                    fre[sets[i]] +=1
        backt(0)
        return res


        