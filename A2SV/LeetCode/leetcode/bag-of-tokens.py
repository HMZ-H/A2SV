class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        score = 0
        while left <= right:
            if tokens[left] <= power:
                score +=1
                power -= tokens[left]
                left +=1
            elif left < right and score >0:
                score -=1
                power += tokens[right]
                right -=1
            else:
                return score
                

        # print(score)
        return score
        