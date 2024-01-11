class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()

        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == k:
                left +=1
                right -=1
                res +=1
            elif nums[left] + nums[right] > k:
                right -=1
            else:
                left +=1
        return res
        