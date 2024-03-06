class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lis = []
        # if target in nums:
        #     lis.append(bisect_left(nums, target))
        #     lis.append(bisect_right(nums, target)-1)
        # else:
        #     lis.append(-1)
        #     lis.append(-1)
        # return lis

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                if nums[left] < target:
                    left +=1
                if nums[right] > target:
                     right -=1
                if nums[left] == target and nums[right] == target:
                    return [left, right]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        if left > right:
            return [-1, -1]
                
                
            



        