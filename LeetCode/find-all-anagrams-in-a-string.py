class Solution:
    def isEqual(self, dics,dics2,s,p):
        for i in dics:
            if i not in p or dics2[i] != dics[i]:
                return False
        return True
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return  []
        result = []
        l, r = 0, len(p)
        dics = defaultdict(int)
        for i in p:
            dics[i] += 1
        dics2 = defaultdict(int)
        for i in range(len(p)):
            dics2[s[i]] += 1
            
        if self.isEqual(dics,dics2,s, p):
            result.append(0)
        # print(dics)
        while r < len(s):
            dics2[s[l]] -= 1
            dics2[s[r]] += 1
            l +=1
            r +=1
            # print(dics2)
            if self.isEqual(dics,dics2,s,p):
                result.append(l)
        return result
