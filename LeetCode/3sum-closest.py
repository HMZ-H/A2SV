class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = sum(nums[:3])
        for i in range(len(nums)-2):

            left = i +1
            right = len(nums)-1

            while left < right:
                closes = nums[i] + nums[left] + nums[right]

                if abs(closes - target) < abs(ans - target):
                    ans = closes
                if closes < target:
                    left +=1
                else:
                    right -=1
        return ans
      