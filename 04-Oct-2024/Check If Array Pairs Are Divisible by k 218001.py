# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0]*k
        for i in arr:
            freq[i%k]+=1
        print(freq)
        if freq[0]%2!=0:
            return False
        for i in range(1,k//2+1):
            if freq[i]!=freq[k-i]:
                return False
        return True