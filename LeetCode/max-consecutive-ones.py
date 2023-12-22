class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # max_1 = 0
        # l, r = 0,0
        
        # while r < len(nums):
        #     curr_max = len(nums[l:r])
        #     max_1 = max(max_1, curr_max)
        #     if nums[r] != 0:
        #         r+=1
        #     elif nums[r] == 0:
        #         l +=2
        #         r+=2
        # if len(nums)==1 and sum(nums) ==1:
        #     return 1
        # return max_1
        count = 0 
        max_count = 0 
        for num in nums:
            if num != 1 :
                max_count = max(max_count , count)
                count = 0 
            else:
                count += 1 
        return max(max_count , count)

        