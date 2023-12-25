class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lis = ''
        tmp = 0
        for i in spaces:
            lis += s[tmp:i]
            lis += " "
            tmp= i
        lis += s[tmp:]
        return lis

        return ' '.join(lis)