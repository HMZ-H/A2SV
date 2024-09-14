# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size, res = 0, 0
        curr_max = 0
        for n in nums:
            if n > curr_max:
                curr_max = n
                size = 1
                res = 0
            elif n == curr_max:
                size += 1
            else:
                size = 0
            res  = max(res, size) 
        return res
