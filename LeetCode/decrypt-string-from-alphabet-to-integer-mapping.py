import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        chars =  string.ascii_lowercase
        codes = ['1','2','3','4','5','6','7','8','9','10#','11#','12#','13#','14#','15#','16#','17#','18#','19#','20#','21#','22#','23#','24#','25#','26#']
        dic = {codes[i]:chars[i] for i in range(26)}
        s = s[::-1]
        position = 0
        result = ''
        while position < len(s):
            if s[position] in dic:
                result+=dic[s[position]]
                position +=1
            else:
                result +=(dic[s[position +2] + s[position +1] +s[position]])
                position +=3
        return result[::-1]

                


        