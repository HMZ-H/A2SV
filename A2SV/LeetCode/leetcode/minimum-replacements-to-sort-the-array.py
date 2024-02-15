class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2, -1,-1):
            if nums[i] <= nums[i+1]:
                continue

            num_of_ele = ceil(nums[i]/nums[i+1])
            res += num_of_ele -1
            nums[i]= nums[i]//num_of_ele
           
        return res
