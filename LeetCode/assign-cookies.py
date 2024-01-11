class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()

        max_ = 0
        right =len(g)-1
        left = len(s)
        left = left -1
        while left >= 0 and right >= 0:
            if s[left] >= g[right]:
                max_ += 1
                left -=1
                right -=1
            else:
                right -=1
        return max_
            