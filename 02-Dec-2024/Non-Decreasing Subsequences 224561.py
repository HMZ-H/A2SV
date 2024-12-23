# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def backtrack(self, subSeq, arr, subSet):
        if len(subSeq) >= 2 and subSeq not in subSet:
            subSet.add(subSeq)
        temp = list(subSeq)
        temp.sort()
        for i in range(len(arr)):
            if len(temp)==0 or (arr[i] >= temp[-1] and tuple(temp+[arr[i]]) not in subSet):
                self.backtrack(tuple(list(subSeq)+[arr[i]]),arr[i+1:],subSet)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = set()
        self.backtrack((),nums,subsequences)
        answer = []
        for s in subsequences:
            answer.append(list(s))
        return answer