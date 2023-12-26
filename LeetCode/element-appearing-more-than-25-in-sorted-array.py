class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # count = Counter(arr)
        # ma = max(count.values())
        # lis = [key for key, value in count.items() if value == ma]
        
        count = Counter(arr)
        res = 0
        ans = 0
        for key, val in count.items():
            if res < val:
                res = val
                ans = key
        return ans
        
        
        
        