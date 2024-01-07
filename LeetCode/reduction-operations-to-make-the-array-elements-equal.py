class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        cout = 0
        res = 0
        curr_el = nums[0]
        for i in range(1, len(nums)):
            if curr_el != nums[i]:
                cout +=1
                res += cout
                curr_el = nums[i]
            else:
                res +=cout
        return res

        

        