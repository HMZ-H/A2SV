class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        strs = sorted(strs)
        fir = strs[0]
        last = strs[-1]
        for _ in range(min(len(fir), len(last))):
            if fir[_] != last[_]:
                return result
            result += fir[_]
        return result
            


            