class Solution:
    def largestOddNumber(self, num: str) -> str:
        # l, r = 0,1
        # odds = 0
        # # if  int(num[l])%2 != 0 and int(num[-1])%2 != 0:
        # #     odds = num
        # while r<len(num)+1:
        #     if int(num[l:r])%2 != 0:
        #         odds = max(int(odds), int(num[l:r]))
        #     r += 1
        # if odds != 0:
        #   return str(odds)
        # else:
        #   return ''
        i = len(num) - 1
        while i >= 0:
            if int(num[i]) % 2 != 0:
                return num[:i+1]
            i -= 1
        return ''


        