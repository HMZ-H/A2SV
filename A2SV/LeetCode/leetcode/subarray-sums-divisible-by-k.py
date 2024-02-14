class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefixSum = 0
        res = 0
        for i in nums:
            prefixSum += i
            s = prefixSum%k
            if s in dic and dic[s] > 0:
                res += dic[s]
            if s in dic:
                dic[s] +=1
            else:

                dic[s] =1
        return res

        