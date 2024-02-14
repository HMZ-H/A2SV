class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_ = 0
        for ar in trips:
            max_ = max(max_, max(ar))
        prefixSum = [0]*(max_+1)
        for p, f, t in trips:
            prefixSum[f] += p
            prefixSum[t] -= p
        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i-1]

        for num in prefixSum:
            if num > capacity:
                return False
        return True


        