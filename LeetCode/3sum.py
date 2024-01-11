class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # dic = defaultdict(list)
        
        # while right < len(nums):
        #     curr_sum = nums[left] + nums[right]
        #     dic[curr_sum] += [nums[left],nums[right]]
        #     left +=1
        #     right +=1

        res = set()
        # j = 0
        for i in range(len(nums)-2):
            right = len(nums)-1
            left = i +1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left +=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    left+=1
        ans = [list(i) for i in res]
        return ans
            

            
            
        

        print(res)
        return
        