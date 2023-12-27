class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
       
        res = {}
        for i in range(len(cpdomains)):
            visit_num = cpdomains[i].split(' ')[0]
            domains = cpdomains[i].split(' ')[1]
            domains = domains.split('.')[::-1]
            k = 1
            while k < len(domains)+1:
                dom = '.'.join(domains[:k][::-1])
                if dom in res:
                    res[dom] += int(visit_num)
                else:
                    res[dom] = int(visit_num)
                k +=1
        ans = []
        for key, value in res.items():
            ans.append(str(value) + ' ' + key)
        return ans

