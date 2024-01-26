class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sumWindow = sum(cardPoints[:len(cardPoints)-k])
        window = len(cardPoints)-k
        all_points = sum(cardPoints)
        ans = 0

        for i in range(k):
            ans = max(ans, all_points-sumWindow)
            sumWindow += cardPoints[i+window]
            sumWindow -= cardPoints[i]
        
        ans = max(ans, all_points-sumWindow)
        return ans