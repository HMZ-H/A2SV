class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right )//2
          
            if letters[mid] > target:
                right = mid 
            else:
                left = mid + 1
        return letters[right] if right < len(letters) else letters[0]
        
        