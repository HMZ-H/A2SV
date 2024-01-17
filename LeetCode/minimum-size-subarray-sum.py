class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0,0
        ans = float('inf')
        n = len(nums)
        for right in range(n):
            total += nums[right]

            while total >= target:
                ans = min(right - left + 1, ans)
                total -= nums[left]
                left +=1
        
        if ans == float('inf'):
            return 0
        else:
            return ans

        