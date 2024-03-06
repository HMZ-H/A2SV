class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        best = right
        while left<=right:
            mid = left + (right - left)//2

            calc_hour = 0

            for i in range(len(piles)):
                calc_hour += ceil(piles[i]/mid)
            if calc_hour <= h:
                best = mid
                right = mid -1
        
            else:
                left = mid +1
                # best = mid
        return best
        