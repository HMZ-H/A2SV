class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        lis = []
        for i, ball in enumerate(boxes):
            if ball == '1':
                lis.append(i)
        ans = []
        for i in range(len(boxes)):
            j = 0
            for index in lis:
                j += abs(i - index)
            ans.append(j)
        return ans
        