class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[i] + nums[i])
        # print(prefixSum)

        dic = defaultdict(int) #{0: 1} 
        dic[0] = 1

        res = 0
        for i in range(1, len(prefixSum)):
            comulative = prefixSum[i] - k
            if comulative in dic:
                res += dic[comulative]
        
            dic[prefixSum[i]] = dic.get(prefixSum[i], 0) + 1
        
        return res
        
        
       

        