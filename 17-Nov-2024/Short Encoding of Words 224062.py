# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # res = set(words)
        # for word in words:
        #     print(res)
        #     for j in range(1, len(word)):
        #         res.discard(word[j:])
        #         print(res.discard(word[j:]))
        # return sum(len(word) + 1 for word in res)

        words.sort(key=len, reverse=True)

        res = ''
        for i in words:
            if i + '#' not in res:
                res += i
                res += '#'
        return len(res)
        