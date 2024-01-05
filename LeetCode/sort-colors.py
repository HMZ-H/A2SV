class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            j = i -1
            curr_val = nums[i]
            while j >= 0 and curr_val > nums[j]:
                nums[j+1] = nums[j]
                j-=1
            j+=1

            if j != i:
                nums[j] = curr_val
        return nums.reverse()


        