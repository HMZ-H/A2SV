class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mdl = 10**9 + 7
        prefixSum = [0]* (len(nums)+1)
        for s, e in requests:
            prefixSum[s] +=1
            prefixSum[e+1] -=1
        for i in range(1,len(prefixSum)):
            prefixSum[i] += prefixSum[i-1]
        prefixSum.sort(reverse=True)
        nums.sort(reverse=True)

        total = 0
        for i in range(len(prefixSum)-1):
            total += (prefixSum[i] * nums[i])%mdl
        return total%mdl
  