class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        frq = len(nums)//3
        result=[]
        for val in count:
            if count[val]>frq:
                result.append(val)
        return result        