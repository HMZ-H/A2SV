# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

import time
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        mins = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]

        mins.sort()

        res = min(mins[i + 1] - mins[i] for i in range(len(mins) -1))

        return min(res, 24 * 60 - mins[-1] + mins[0])
        
        