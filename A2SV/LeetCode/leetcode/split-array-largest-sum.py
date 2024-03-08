class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        best = max(nums)
        
        while left <= right:
            mid = left + (right - left)//2
            cout = 0
            kk = 1

            for i in range(len(nums)):
                cout += nums[i]
 
                if cout > mid:
                    cout = nums[i]
                    kk +=1
            if kk>k:
                left = mid +1
            else:
                right = mid - 1
                best = mid
        return best