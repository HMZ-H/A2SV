class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_le = 0

        for num in num_set:
            if num -1 not in num_set:
                curr_num = num
                curr_len = 1

                while curr_num +1 in num_set:
                    curr_num +=1
                    curr_len +=1
                max_le = max(max_le, curr_len)
        return max_le
    