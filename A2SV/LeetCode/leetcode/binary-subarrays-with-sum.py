class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0:1}
        
        prefixSum = 0
        cout = 0
        for i in nums:
            prefixSum +=i 
            dif = prefixSum - goal
            if dif in dic:
                cout +=dic[dif]
            if prefixSum in dic:
                dic[prefixSum] +=1
            # if dif in dic:
            else:
                dic[prefixSum] = 1
            print(prefixSum)
        return cout
        
