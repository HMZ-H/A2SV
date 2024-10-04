# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []
        for word in words:
           
            mappings = dict()
            mapped = set()
            i, j = 0, 0
            while i < len(word) and j < len(pattern):
                mapping = mappings.get(pattern[j])
                if mapping is not None:
                   
                    if mapping != word[i]:
                        break
                else:
                   
                    if word[i] not in mapped:
                        mappings[pattern[j]] = word[i]
                        mapped.add(word[i])
                    else:
                        break
                i += 1
                j += 1

            if i == len(word):
                matches.append(word)

        return matches      