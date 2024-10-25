# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:

    # def search(text, pattern):

    #     lps = [0]*len(pattern)

    #     i = 0
    #     j = 1

    #     while j <= len(pattern):
    #         if pattarn[j] == pattern[i]:
    #             i += 1
    #             lps[j] = i
    #             j += 1
    #         else:
    #             if i != 0:
    #                 i = lps[i - 1]
    #             else:
    #                 j += 1
        
    #     #searching
    #     i = 0
    #     j = 0

    #     while i <= len(text):
    #         if pattern[j] == text[i]:
    #             i += 1
    #             j += 1

    #         if j == len(pattern):
    #             return True
    #         elif i < len(text) and text[i] != pattern[j]:
    #             if j != 0:
    #                 j = lps[j-1]

    #             else:
    #                 i += 1

    #     return False
    

    def repeatedStringMatch(self, a: str, b: str) -> int:

        # min_repeat = (len(b) + len(a) - 1)// len(a)

        # s = a * min_repeat

        # if search(s, b):
        #     return min_repeat

        # s += a
        # if search(s, b):
        #     return min_repeat + 1
        # return -1

        repeat = len(b)//len(a)
        count = 1

        while count <= repeat + 2:
            if b  in a*count:
                return count 
            else:
                count += 1
        return -1













            
        