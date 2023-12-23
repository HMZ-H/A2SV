class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l, r = 0, 1
        res = []
        while r < len(nums):
            res.extend([nums[r]]*nums[l])
            l+=2
            r+=2
        return res

        