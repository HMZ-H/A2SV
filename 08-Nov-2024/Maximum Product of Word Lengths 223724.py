# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        temp = []
        bits = [["0" for i in range(26)] for i in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words[i])):
                bits[i][ord(words[i][j])-ord('a')] = "1"
            temp.append(int("".join(bits[i]),2))
        ans = 0
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                if temp[i]&temp[j] == 0:
                    ans = max(ans,len(words[i]) * len(words[j]))
        return ans
                