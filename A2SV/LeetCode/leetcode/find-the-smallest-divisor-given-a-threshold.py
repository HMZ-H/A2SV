class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right  = 1, max(nums)
        while left<=right:
            mid = left + (right - left)//2

            curr = 0
            for i in nums:
                curr += ceil(i/mid)
            if curr >threshold:
                left = mid + 1
            else:
                right = mid -1
        return left
            


        