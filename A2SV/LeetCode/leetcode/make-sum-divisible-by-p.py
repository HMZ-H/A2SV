class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0
        
        target = sum(nums) % p
        remainder = {0: -1}
        curr = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            curr = (curr + num) % p
            complement = (curr - target) % p
            
            if complement in remainder:
                min_length = min(min_length, i - remainder[complement])
            
            remainder[curr] = i
        
        return min_length if min_length < len(nums) else -1