class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre = Counter(s)
        result = []
        for key, value in fre.items():
            if value == 1:
                result.append(s.index(key))
                break
        if len(result) != 0:
            return result[0]
        else:
            return -1
            
        

        