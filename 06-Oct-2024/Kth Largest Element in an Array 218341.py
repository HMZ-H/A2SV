# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = heapify(nums)
        # print(heap)
        # arr = [ i*-1 for i in nums]
        for i in range(len(nums)):
            nums[i] *= -1

        heapify(nums)
        curr = 0
        while k > 0:
            curr = heappop(nums)
            k -= 1

        return curr*-1
        