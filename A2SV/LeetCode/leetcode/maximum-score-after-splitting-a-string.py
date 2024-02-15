class Solution:
    def maxScore(self, s: str) -> int:
        zeroPrefix = [0]* (len(s)+1)
        onePrefix = [0] *(len(s)+1)
        cout_0 = 0 
        cout_1 = 0
        for i in range(len(s)):
            
            if s[i] == '0':
                cout_0 +=1
                zeroPrefix[i] += (cout_0)
                onePrefix[i] = cout_1
            elif s[i] == '1':
                cout_1 +=1
                zeroPrefix[i] = cout_0
                onePrefix[i] += (cout_1)
        max_res = 0
        for i in range(len(zeroPrefix)-2):
            max_res = max(max_res, onePrefix[-2] + zeroPrefix[i] - onePrefix[i])

            # print(max_res)
        return max_res
        