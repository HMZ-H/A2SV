class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_len = 0
        
        max_cout = 0
        max_consecutive = 0

        fre = defaultdict(int)
        left, right = 0,0
        while right < len(answerKey):
            fre[answerKey[right]] += 1
            max_cout = max(max_cout, fre[answerKey[right]])

            if (right - left + 1)  - max_cout > k:
                fre[answerKey[left]] -=1
                left +=1
            max_consecutive = max(max_consecutive, right - left + 1)
            right +=1
        return max_consecutive
        