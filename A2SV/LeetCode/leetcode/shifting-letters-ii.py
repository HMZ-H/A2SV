class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 
                    't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        n = len(s)
        lis = [0]*n
        for st, e, d in shifts:
            if d == 0:
                lis[st] -= 1 
                if e + 1 < n:
                    lis[e+1] +=1
            else:
                lis[st] += 1 
                if e + 1 < n:
                    lis[e+1] -=1
        for i in range(1, n):
            lis[i] += lis[i-1]
        for i in range(len(lis)):
            lis[i] = list(letters.keys())[(letters[s[i]] + lis[i])%26]

        return ''.join(lis)
       