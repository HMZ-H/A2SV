class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        max_score, curr_sum = 0, 0
        right = 0
        for i, j in enumerate(nums):
            if j in seen:
                while right < seen[j]+1:
                    curr_sum -= nums[right]
                    right +=1
            seen[j] = i
            curr_sum += j
            max_score = max(max_score, curr_sum)
        return max_score

        

        