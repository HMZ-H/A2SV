class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.reverse()
        # if len(citations) <= citations[-1]:
        #     return len(citations)
        # for i in range(len(citations)):
        #     if citations[i] < i + 1:
        #         return i
        # return 0
        if len(citations) == 1 and citations[0] > 0:
            return 1
        if citations[-1] == 0:
            return 0
        if len(citations)<= citations[0]:
            return len(citations)
        left, right = 0, len(citations)
        best = 0
        while left <= right:
            mid = left + (right - left)//2
            if mid>= citations[len(citations) - mid -1]:
                best = mid
                right = mid -1
            else:
                left = mid +1
        return best
