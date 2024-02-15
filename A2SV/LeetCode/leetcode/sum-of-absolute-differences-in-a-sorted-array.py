class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*(n+1)
        for i in range(n):
            pref[i] += pref[i-1] + nums[i]
        pref = pref[:-1]
        sufix = [0]
        for i in range(n-1,-1,-1):
            sufix.append(sufix[-1] + nums[i])
        sufix = sufix[::-1][:-1]
        print(pref, sufix)
        res = []
        for i in range(n):
            left_sum = nums[i]*i - pref[i]
            right_sum = sufix[i] - (nums[i]*(n-i-1))
            res.append(right_sum + left_sum )
        return res



        