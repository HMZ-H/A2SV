class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, i = 1, 0
        add = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i +=1
            else:
                miss *= 2
                add +=1
            # print(nums)
        return add
        