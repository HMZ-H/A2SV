# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans= []
        dic = {}
        num = sorted(nums)
        for i in range(len(nums)):
            if num[i] not in dic:
                dic[num[i]] = i
        for j in range(len(nums)):
            ans.append(dic[nums[j]])
        return ans
                