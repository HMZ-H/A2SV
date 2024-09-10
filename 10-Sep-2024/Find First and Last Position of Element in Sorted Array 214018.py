# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if target in nums:
        #     return [bisect_left(nums, target), bisect_right(nums, target) -1]
        # else:
        #     return [-1,-1]
        
        left = self.bs(nums, target, True)
        right = self.bs(nums, target, False)
        return [left, right]
        
    def bs(self, nums, target, leftbias):
        low, high = 0, len(nums)-1
        i = -1
        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:
                i = mid
                if leftbias:
                    high = mid -1
                else:
                    low = mid + 1
        return i 




                
