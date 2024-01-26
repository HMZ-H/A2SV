class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for right in range(1, len(nums)):
            left = right -1
            curr_val = nums[right]
            while left >= 0 and curr_val > nums[left]:
                nums[left+1] = nums[left]
                left-=1
            left+=1

            if left != right:
                nums[left] = curr_val
        return nums.reverse()


        