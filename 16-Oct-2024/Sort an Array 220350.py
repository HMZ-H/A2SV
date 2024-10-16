# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half, right_half):
            left = 0
            right = 0
            res = []
            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    res.append(left_half[left])
                    left +=1
                else:
                    res.append(right_half[right])
                    right +=1
            res.extend(left_half[left:])
            res.extend(right_half[right:])
            return res
            # print(res)
        def mergeSort(left, right, nums):
            if left >= right:
                return [nums[left]]
            mid = left + (right - left)//2
            left_half = mergeSort(left, mid, nums)
            right_half = mergeSort(mid+1, right, nums)
            return merge(left_half, right_half)
        return mergeSort(0, len(nums)-1, nums)

        

        

        