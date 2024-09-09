# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for i in range(n+1):
            temp = bin(i)[2:]
            res.append(temp.count("1"))

        return res
        
        