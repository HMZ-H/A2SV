class Solution:
    def reverseWords(self, s: str) -> str:
        lis = []
        words = s.rstrip().lstrip().split(' ')
        lis = [i for i in words if i != '']
        return ' '.join(lis[::-1])
        