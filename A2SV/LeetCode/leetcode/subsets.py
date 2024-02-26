class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lis = [[]]
        def backt(start, path):
            for num in range(start, len(nums)):
                path.append(nums[num])
                lis.append(path.copy())
                backt(num + 1, path)
                path.pop()
            
        backt(0, [])
        # print(lis)
        return lis