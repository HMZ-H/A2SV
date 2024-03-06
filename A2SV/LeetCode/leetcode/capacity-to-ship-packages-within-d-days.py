class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, best = max(weights), sum(weights), -1
        while left<=right:
            mid = left + (right - left)//2

            calc_day = 1
            cout = 0
            for i in range(len(weights)):
                cout += weights[i]
                if cout > mid:
                    calc_day +=1
                    cout = weights[i]
            if calc_day > days:
                left = mid +1
            else:
                right = mid -1
                best = mid
        return best

        