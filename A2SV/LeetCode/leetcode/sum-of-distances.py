class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i, val in enumerate(nums):
            dic[val].append(i)
        
        res = [0] * len(nums)
        for i in dic:
            l = dic[i]
            pre = [0]
            for x in l:
                pre.append(pre[-1] + x)
            for i, x in enumerate(l):
                left = x * (i + 1) - pre[i + 1]
                right = pre[-1] - pre[i] - x * (len(l) - i)
                res[x] = left + right
        
        return res
            