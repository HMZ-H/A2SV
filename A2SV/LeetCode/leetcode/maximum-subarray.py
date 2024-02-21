class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            max_sum = max(max_sum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return max_sum