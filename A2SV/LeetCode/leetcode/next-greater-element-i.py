class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        cout = 0
        dic = defaultdict(lambda: -1)
        for i in nums2:
            while stack and stack[-1]<i:
                dic[stack[-1]] = i
                stack.pop()
            stack.append(i)
        return [dic[i] for i in nums1]

        return lis
        