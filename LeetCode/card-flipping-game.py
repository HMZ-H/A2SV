class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        alls = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in alls:
                alls.remove(fronts[i])
        if len(alls) == 0:
            return 0
        else:
            return alls.pop()


        