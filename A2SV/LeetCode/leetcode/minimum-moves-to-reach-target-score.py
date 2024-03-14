class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if maxDoubles:
                print(res, target)
                res += ceil((target/2) - (target//2)) +1
                maxDoubles -= 1
                target = target//2
            else:
                res += target -1
                return res
        return res
        
        