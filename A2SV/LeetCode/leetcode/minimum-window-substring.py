class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        fre_t = defaultdict(int)
        window = defaultdict(int)
        left = 0
        for char in t:
            fre_t[char] +=1
        
        have, need = 0, len(fre_t)
        res, len_res = [-1, -1], float('inf')
        for right in range(len(s)):
            char = s[right]
            window[char] +=1
            if char in fre_t and window[char] == fre_t[char]:
                have +=1
            while have == need:
                if right - left + 1 < len_res:
                    res = [left, right]
                    len_res = right - left + 1
                window[s[left]] -=1
                if s[left] in fre_t and window[s[left]] < fre_t[s[left]]:
                    have -=1
                left +=1
        left, right = res
        return s[left: right +1] if len(s) != float('inf') else ""



        
        