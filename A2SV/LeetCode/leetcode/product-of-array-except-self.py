class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]*len(nums)
        l = 1
        for i in range(len(nums)):
            product[i] = l
            l *= nums[i]
        l = 1
        for i in range(len(nums)-1, -1,-1):
            product[i] *= l
            l *= nums[i]
        return product
        