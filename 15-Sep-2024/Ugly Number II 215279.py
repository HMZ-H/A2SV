# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        visit = set()
        factorial = [2,3,5]

        for i in range(n):
            num = heappop(min_heap)
            if i == n - 1:
                return num

            for f in factorial:
                if num*f not in visit:
                    visit.add(num*f)
                    heappush(min_heap, num*f)