class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_rob = 0
        # right = 0
        # while right <= len(nums):
        #     curr_sum = 0
        #     for i in range(right,len(nums),2):
        #         curr_sum += nums[i]
        #     max_rob = max(max_rob, curr_sum)
        #     right +=1

        # return max_rob
        if len(nums) == 1:
            return nums[0]
        sums = nums[0]
        birr = nums[1]
        for i in range(2, len(nums)):
            if i%2 == 0:
                birr = max(birr, sums)
                sums += nums[i]
            else:
                sums = max(birr, sums)
                birr += nums[i]
        return max(birr, sums)

        