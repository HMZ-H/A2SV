class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]
        for i in nums:
            res.append(i+res[-1])
        return res[1:]
        # l = nums[0]
        # res = []
        # res.append(l)
        # for i in range(1, len(nums)):
        #     res.append(res[-1] + nums[i])
        # return res