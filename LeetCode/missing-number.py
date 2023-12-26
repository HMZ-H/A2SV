class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ran = [i for i in range(len(nums)+1)]
        miss = 0
        for i in ran:
            if i not in nums:
                miss+=i
        return miss

        