# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for key, value in enumerate(nums):
            r = target - value
            if r in dic: 
                return [dic[r], key]
            dic[value] = key

        