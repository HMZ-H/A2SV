class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        if target in nums:
            return bisect_left(nums, target)
        else:
            return -1
        