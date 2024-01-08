class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        # dic = defaultdict(int)
        # for i in range(len(nums)+1):
        #     dic[i] = nums[:i].count(0) + nums[i:].count(1)
        # max_value = max(dic.values())

        # res =[]
        # for key, value in dic.items():
        #     if value == max_value:
        #         res.append(key)
        
        # return res

        l, r = 0, sum(nums)
        res = [0]
        max_ = r

        for i in range(len(nums)):
            if nums[i] == 0:
                l += 1
            else:
                r -= 1
            s = l + r

            if s == max_:
                res.append(i +1)
            elif s>max_:
                res = []
                res.append(i + 1)
                max_ = s
        return res

            
        