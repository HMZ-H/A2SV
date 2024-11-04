# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:    
    def decodeString(self, s: str) -> str:
        def rec( i , n,l):
            if  i >= len(s):
                return ""
            if s[i] == ']':
                l[0] = i
                return ""
            if s[i] == '[':
                return int(n)*rec(i+1, "", l) + rec(l[0]+1, "", l)
            if s[i].isdigit():
                return rec(i+1, n+s[i], l)
            else:
                return s[i] + rec(i+1, n, l)
        l = [0]
        return rec(0, "", l)