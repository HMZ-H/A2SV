class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        lis = [0]*len(words)
        for i in range(len(words)):
            lis[(int(words[i][-1])-1)] = (words[i][:-1])
     
        return ' '.join(lis)

        