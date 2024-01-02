class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        tra = [list(i) for i in list(zip(*strs))]
        for i in tra:
            if ''.join(sorted(i)) != ''.join(i):
                res +=1
        return res