class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window  =  sum(nums[:k])
        max_avg = window/k
        l = 0
        while l < len(nums)-k:
            window = window - nums[l] + nums[l + k]
            max_avg = max(max_avg, window/k)
            l +=1
        
        return max_avg
