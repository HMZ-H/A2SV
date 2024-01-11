class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cout = 0
        nums.sort()
         
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < target:
        #             cout +=1
        # for i in range(len(nums)):
        #     while 
        left, right = 0, len(nums) -1
        while left < right:
            if nums[left] + nums[right] < target:
                cout += right - left
                left +=1
            else:
                right -=1

            
        return cout
        