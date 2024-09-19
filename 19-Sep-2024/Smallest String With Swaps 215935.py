# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = [i for i in range(len(s))]

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            parents[find(x)] = find(y)

        for x, y in pairs:
            union(x, y)
        
        
        dic_i = defaultdict(list)
        dic_chr = defaultdict(list)

        for i in range(len(s)):
            par = find(i)

            dic_i[par].append(i)
            dic_chr[par].append(s[i])
        res = ['']*len(s)

        for x in dic_i.keys():
            ind = sorted(dic_i[x])
            chars = sorted(dic_chr[x])
            for i, c in zip(ind, chars):
                res[i] = c
       
        return ''.join(res)

        
        