class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lis = [[]]
        def backt(start, path):
            for num in range(start, len(nums)):
                path.append(nums[num])
                y = (sorted(path.copy()))
                if  not y in lis:
                    lis.append(y)
                
                backt(num + 1, path)
                path.pop()
                print(path)
            
        backt(0, [])
        return lis