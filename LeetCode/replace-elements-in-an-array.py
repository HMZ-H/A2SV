class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapp = {}
        for i, x in enumerate(nums):
            mapp[x] = i
        for x in operations:
            nums[mapp[x[0]]] = x[1]
            mapp[x[1]] = mapp[x[0]]
            del mapp[x[0]]
        
        return nums