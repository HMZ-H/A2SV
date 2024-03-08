class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        curr  =  float('inf')
        stack = []
        for num in nums:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True
            stack.append((num, curr))
            curr = min(curr, num)
        return False
        