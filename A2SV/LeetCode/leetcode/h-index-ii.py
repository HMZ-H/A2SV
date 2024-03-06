class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.reverse()
        if len(citations) == 1 and citations[0] > 0:
            return 1
        if len(citations) <= citations[-1]:
            return len(citations)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return 0