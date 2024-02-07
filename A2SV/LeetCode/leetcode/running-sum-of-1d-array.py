class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]
        for i in nums:
            res.append(i+res[-1])
        return res[1:]