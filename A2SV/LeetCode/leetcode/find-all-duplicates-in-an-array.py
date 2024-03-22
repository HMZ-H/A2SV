class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # fre = Counter(nums)
        # res = []
        # for key, val in fre.items():
        #     if val > 1:
        #         res.append(key)
        # return res
        n = len(nums)
        i = 0
        while i < n:
            curr_ind = nums[i]
            if curr_ind != i+1 and nums[curr_ind-1] != curr_ind :
                nums[curr_ind-1], nums[i] = nums[i], nums[curr_ind-1]
            else:
                i +=1
        res = set()
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.add(nums[i])
        return res
       