class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        fre = Counter(answers)
        res = 0
        for key in fre:
            val = fre[key]
            temp = key + 1
            res += ceil(val/temp)*temp
        return res


        