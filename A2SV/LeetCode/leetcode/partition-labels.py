class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        n = len(s)
        for i in range(n):
            dic[s[i]] = i

        anchor, j = 0,0 
        res = []
        for i in range(n):
            j = max(j, dic[s[i]])
            if i ==j:
                res.append(i - anchor + 1)
                anchor = i+1
        return res
        