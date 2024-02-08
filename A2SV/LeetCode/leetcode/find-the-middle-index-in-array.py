class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        totalSum = sum(nums)
        if totalSum - nums[0] == 0:
            return 0
        for i in range(1, n):
            nums[i] += nums[i-1]
            if nums[i-1] == totalSum - nums[i]:
                return i
        else:
            return -1