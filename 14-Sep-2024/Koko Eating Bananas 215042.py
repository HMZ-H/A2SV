# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        res = right 
        while left <= right:
            mid = left + (right - left)//2

            hours = 0
            for p in piles:
                hours += ceil(p/mid)
            if hours <= h:
                res = min(res, mid)
                right = mid -1
            else:
                left = mid + 1
        return res

        