class Solution:
    def longestPalindrome(self, s: str) -> int:
        fre = Counter(s)
        res = 0
        od_m_ = 0
        for i in fre:
            if fre[i]%2 != 0:
                if od_m_ < fre[i]:
                    res += max(od_m_-1, 0)
                    od_m_ = fre[i]
                else:
                    res += fre[i] -1 
            else:
                res += fre[i]
        return res + od_m_
        