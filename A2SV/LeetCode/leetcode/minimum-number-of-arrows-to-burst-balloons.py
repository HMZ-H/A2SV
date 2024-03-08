class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arr = sorted(points, key=lambda x: x[1])
        res = 1
        curr = arr[0][1]
        for i in range(1, len(points)):
            if curr < arr[i][0]:
                res +=1
                curr = arr[i][1]
        # print(res)
        return res
        