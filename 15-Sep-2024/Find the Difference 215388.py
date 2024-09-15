# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in t:
            ans += ord(c)

        for c in s:
            ans -= ord(c)           
        return chr(ans)
        