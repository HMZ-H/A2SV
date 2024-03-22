class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            curr_ind = nums[i]
            if curr_ind != i+1 and nums[curr_ind-1] != curr_ind :
                nums[curr_ind-1], nums[i] = nums[i], nums[curr_ind-1]
            else:
                i +=1
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res