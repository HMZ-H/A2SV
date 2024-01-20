class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        # while right < len(nums):
        #     if nums[right] != 0 and zeros != 0:
        #         right +=1
        #     if nums[right] == 0 and zeros == 1:
        #         zeros -=1
        #         right +=1
        #     if nums[right] == 0 and zeros == 0:
        #         max_len = max(max_len, right - left + 1)
        #         left +=1
        #         # zeros = 1
        # print(max_len)
        # return 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros +=1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left +=1
            max_len = max(max_len, right - left)
        return max_len
        